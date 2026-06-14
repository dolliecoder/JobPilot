from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.db import Base

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    status = Column(String, default="Applied")  # Applied, Interviewing, Rejected, Accepted
    applied_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    resume = relationship("Resume", foreign_keys=[resume_id])
    job = relationship("Job", foreign_keys=[job_id])
    
    def __repr__(self):
        return f"<Application(id={self.id}, resume_id={self.resume_id}, job_id={self.job_id}, status={self.status})>"
