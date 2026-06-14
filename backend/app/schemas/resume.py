from pydantic import BaseModel
from datetime import datetime
from typing import List

class ResumeResponse(BaseModel):
    id: int
    filename: str
    file_path: str
    uploaded_at: datetime
    
    class Config:
        from_attributes = True

class ResumeList(BaseModel):
    resumes: List[ResumeResponse]
