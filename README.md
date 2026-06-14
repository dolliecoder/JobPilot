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

✅ **Application Management**
- Apply to jobs with uploaded resume
- Select which resume to use for each application
- View all applications in one place
- Track application status (Applied, Interviewing, Accepted, Rejected)
- Delete applications
- Duplicate application prevention

🔜 **Coming Soon**
- AI-powered resume matching
- Application analytics

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
   - Upload your PDF resume (max 5MB)
   - View all uploaded resumes
   - Delete resumes you no longer need

2. **Browse Jobs**: Go to http://localhost:3000/jobs
   - View 15 sample job listings
   - Search by keywords (e.g., "python", "react", "java", ".net")
   - Filter by company, location, or job type

3. **Apply to Jobs**: 
   - Click "Apply" button on any job
   - Select which resume to use
   - Submit your application

4. **Track Applications**: Go to http://localhost:3000/applications
   - View all your applications
   - See status (Applied, Interviewing, Accepted, Rejected)
   - Track when you applied
   - Delete applications if needed

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
