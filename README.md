# AI Job Application System

A full-stack application for managing job applications with AI-powered features.

## Tech Stack

- **Frontend**: Next.js 15 (TypeScript)
- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy

## Features Implemented

✅ **Resume Management**
- Upload PDF resumes (max 5MB)
- View uploaded resumes
- Delete resumes
- File storage in uploads directory

✅ **Job Search**
- Browse 15+ sample job listings
- Search by keyword (title, company, location, job type)
- Real-time filtering
- Jobs for Java, Python, .NET, React, Full Stack developers

🔜 **Coming Soon**
- Job application tracking
- AI-powered resume matching
- Application status management

## Project Structure

```
job-application-system/
├── frontend/          # Next.js frontend application
├── backend/           # FastAPI backend application
├── README.md
└── .gitignore
```

## Getting Started

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.database.init_db
python -m app.database.seed_jobs  # Seed sample jobs
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Usage

1. **Upload Resume**: Go to http://localhost:3000/upload
2. **Browse Jobs**: Go to http://localhost:3000/jobs
3. **Search Jobs**: Enter keywords like "python", "react", "java", ".net"

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Sample Jobs

The system includes 15 sample jobs for:
- Java Developer
- Full Stack Developer
- Python Developer
- .NET Developer
- React Developer
- And more...

## Testing

Run the verification script:
```bash
python verify_startup.py
```
