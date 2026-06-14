from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeResponse, ResumeList
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """Upload a resume file (PDF only, max 5MB)"""
    
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    
    # Read file content to check size
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds maximum allowed size of 5MB"
        )
    
    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    original_filename = file.filename
    safe_filename = f"{timestamp}_{original_filename}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)
    
    # Save file
    try:
        with open(file_path, "wb") as f:
            f.write(content)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save file: {str(e)}"
        )
    
    # Create database record
    resume = Resume(
        filename=original_filename,
        file_path=file_path
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    
    return resume

@router.get("/", response_model=ResumeList)
async def list_resumes(db: Session = Depends(get_db)):
    """List all uploaded resumes ordered by upload date (newest first)"""
    resumes = db.query(Resume).order_by(Resume.uploaded_at.desc()).all()
    return {"resumes": resumes}

@router.get("/{resume_id}", response_model=ResumeResponse)
async def get_resume(resume_id: int, db: Session = Depends(get_db)):
    """Get a specific resume by ID"""
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resume

@router.delete("/{resume_id}")
async def delete_resume(resume_id: int, db: Session = Depends(get_db)):
    """Delete a resume (database record and physical file)"""
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    # Delete physical file
    try:
        if os.path.exists(resume.file_path):
            os.remove(resume.file_path)
    except Exception as e:
        print(f"Warning: Failed to delete file {resume.file_path}: {str(e)}")
    
    # Delete database record
    db.delete(resume)
    db.commit()
    
    return {"message": f"Resume '{resume.filename}' deleted successfully"}
