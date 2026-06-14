# AI Job Application System

A full-stack application for managing job applications with AI-powered features.

## Tech Stack

- **Frontend**: Next.js 15 (TypeScript)
- **Backend**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy

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
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Documentation

Once the backend is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
