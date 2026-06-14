from app.database.db import engine, Base
from app.models import resume, job, application
import os

def init_db():
    """Initialize database tables"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    
    # Create uploads directory
    upload_dir = os.getenv("UPLOAD_DIR", "./uploads")
    os.makedirs(upload_dir, exist_ok=True)
    print(f"Upload directory created at: {upload_dir}")

if __name__ == "__main__":
    init_db()
