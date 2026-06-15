from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import resumes, jobs, applications
from app.database.db import engine, Base
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database tables on application startup"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully")
    except Exception as e:
        print(f"Warning: Database initialization error: {e}")
    yield


app = FastAPI(
    title="AI Job Application System",
    description="Backend API for AI-powered job application management",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS configuration for Next.js frontend (localhost for dev, Vercel for production)
cors_origins = [
    "http://localhost:3000",
    "https://job-pilot-67bvb1nj-dollychahar27-6796s-projects.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(resumes.router, prefix="/api/resumes", tags=["resumes"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])
app.include_router(applications.router, prefix="/api/applications", tags=["applications"])

@app.get("/")
async def root():
    return {
        "message": "AI Job Application System API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
