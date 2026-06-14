from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.sql import func
from app.database.db import Base

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    match_score = Column(Float, nullable=True)
    status = Column(String, default="pending")  # pending, applied, rejected
    applied_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<Application(id={self.id}, resume_id={self.resume_id}, job_id={self.job_id})>"
