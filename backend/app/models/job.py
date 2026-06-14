from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database.db import Base

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    company = Column(String, nullable=False)
    location = Column(String, nullable=False)
    job_type = Column(String, nullable=False)  # Full-time, Part-time, Contract, etc.
    description = Column(Text, nullable=False)
    requirements = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    
    def __repr__(self):
        return f"<Job(id={self.id}, title={self.title}, company={self.company})>"
