from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    job_type: str
    description: str
    requirements: Optional[str] = None
    created_at: datetime
    
    class Config:
        from_attributes = True

class JobList(BaseModel):
    jobs: List[JobResponse]

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    job_type: str
    description: str
    requirements: Optional[str] = None
