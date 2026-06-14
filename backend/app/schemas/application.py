from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ApplicationCreate(BaseModel):
    resume_id: int
    job_id: int

class ApplicationResponse(BaseModel):
    id: int
    resume_id: int
    job_id: int
    status: str
    applied_at: datetime
    
    # Nested data for easier frontend display
    job_title: Optional[str] = None
    job_company: Optional[str] = None
    resume_filename: Optional[str] = None
    
    class Config:
        from_attributes = True

class ApplicationList(BaseModel):
    applications: List[ApplicationResponse]
