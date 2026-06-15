import logging
import traceback
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database.db import get_db
from app.models.job import Job
from app.schemas.job import JobResponse, JobList, JobCreate
from typing import Optional

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=JobResponse)
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """Create a new job posting"""
    db_job = Job(
        title=job.title,
        company=job.company,
        location=job.location,
        job_type=job.job_type,
        description=job.description,
        requirements=job.requirements
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/", response_model=JobList)
async def list_jobs(
    keyword: Optional[str] = Query(None, description="Search keyword for title, company, or location"),
    db: Session = Depends(get_db)
):
    """List all job postings with optional keyword search"""
    try:
        logger.info("list_jobs called, executing query...")
        query = db.query(Job)
        logger.info(f"Query object created: {query}")
        
        # Filter by keyword if provided
        if keyword:
            search_term = f"%{keyword}%"
            query = query.filter(
                or_(
                    Job.title.ilike(search_term),
                    Job.company.ilike(search_term),
                    Job.location.ilike(search_term),
                    Job.job_type.ilike(search_term)
                )
            )
        
        jobs = query.order_by(Job.created_at.desc()).all()
        logger.info(f"list_jobs succeeded, returned {len(jobs)} jobs")
        return {"jobs": jobs}
    except Exception as e:
        logger.error(f"list_jobs FAILED: {type(e).__name__}: {e}")
        logger.error(f"Traceback:\n{traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {type(e).__name__}: {str(e)}")

@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get a specific job by ID"""
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/{job_id}", response_model=JobResponse)
async def update_job(job_id: int, job: JobCreate, db: Session = Depends(get_db)):
    """Update a job posting"""
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db_job.title = job.title
    db_job.company = job.company
    db_job.location = job.location
    db_job.job_type = job.job_type
    db_job.description = job.description
    db_job.requirements = job.requirements
    
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    """Delete a job posting"""
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    db.delete(job)
    db.commit()
    return {"message": f"Job '{job.title}' deleted successfully"}
