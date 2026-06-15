import logging
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import resumes, jobs, applications
from app.database.db import engine, Base, SessionLocal, init_db_tables, seed_jobs_if_empty
import os

# Configure logging to stdout so Render captures it
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stdout,
    force=True,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database tables and seed data on application startup."""
    try:
        tables = init_db_tables()
        logger.info(f"Database initialized with tables: {tables}")

        # Seed sample jobs if empty (using a dedicated session)
        db = SessionLocal()
        try:
            seed_jobs_if_empty(db)
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Startup initialization failed: {type(e).__name__}: {e}")
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
