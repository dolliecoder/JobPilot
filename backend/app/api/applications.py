from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.application import Application
from app.models.job import Job
from app.models.resume import Resume
from app.schemas.application import ApplicationResponse, ApplicationList, ApplicationCreate

router = APIRouter()

@router.post("/", response_model=ApplicationResponse)
async def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db)
):
    """Create a new job application"""
    
    # Check if resume exists
    resume = db.query(Resume).filter(Resume.id == application.resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    # Check if job exists
    job = db.query(Job).filter(Job.id == application.job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Check if application already exists
    existing = db.query(Application).filter(
        Application.resume_id == application.resume_id,
        Application.job_id == application.job_id
    ).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="You have already applied to this job with this resume"
        )
    
    # Create application
    db_application = Application(
        resume_id=application.resume_id,
        job_id=application.job_id,
        status="Applied"
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    
    # Add nested data for response
    response = ApplicationResponse(
        id=db_application.id,
        resume_id=db_application.resume_id,
        job_id=db_application.job_id,
        status=db_application.status,
        applied_at=db_application.applied_at,
        job_title=job.title,
        job_company=job.company,
        resume_filename=resume.filename
    )
    
    return response

@router.get("/", response_model=ApplicationList)
async def list_applications(db: Session = Depends(get_db)):
    """List all job applications with job and resume details"""
    applications = db.query(Application).order_by(Application.applied_at.desc()).all()
    
    # Build response with nested data
    response_list = []
    for app in applications:
        job = db.query(Job).filter(Job.id == app.job_id).first()
        resume = db.query(Resume).filter(Resume.id == app.resume_id).first()
        
        response_list.append(ApplicationResponse(
            id=app.id,
            resume_id=app.resume_id,
            job_id=app.job_id,
            status=app.status,
            applied_at=app.applied_at,
            job_title=job.title if job else "Unknown",
            job_company=job.company if job else "Unknown",
            resume_filename=resume.filename if resume else "Unknown"
        ))
    
    return {"applications": response_list}

@router.get("/{application_id}", response_model=ApplicationResponse)
async def get_application(application_id: int, db: Session = Depends(get_db)):
    """Get a specific application by ID"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    job = db.query(Job).filter(Job.id == application.job_id).first()
    resume = db.query(Resume).filter(Resume.id == application.resume_id).first()
    
    return ApplicationResponse(
        id=application.id,
        resume_id=application.resume_id,
        job_id=application.job_id,
        status=application.status,
        applied_at=application.applied_at,
        job_title=job.title if job else "Unknown",
        job_company=job.company if job else "Unknown",
        resume_filename=resume.filename if resume else "Unknown"
    )

@router.put("/{application_id}/status", response_model=ApplicationResponse)
async def update_application_status(
    application_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    """Update application status"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    application.status = status
    db.commit()
    db.refresh(application)
    
    job = db.query(Job).filter(Job.id == application.job_id).first()
    resume = db.query(Resume).filter(Resume.id == application.resume_id).first()
    
    return ApplicationResponse(
        id=application.id,
        resume_id=application.resume_id,
        job_id=application.job_id,
        status=application.status,
        applied_at=application.applied_at,
        job_title=job.title if job else "Unknown",
        job_company=job.company if job else "Unknown",
        resume_filename=resume.filename if resume else "Unknown"
    )

@router.delete("/{application_id}")
async def delete_application(application_id: int, db: Session = Depends(get_db)):
    """Delete an application"""
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    db.delete(application)
    db.commit()
    return {"message": "Application deleted successfully"}
