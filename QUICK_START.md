# Quick Start Guide

## 🚀 Start the Application

### Terminal 1 - Backend
```bash
cd backend
python -m uvicorn app.main:app --reload
```

### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```

## 🌐 Access URLs

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

## ✅ Verify Everything Works

```bash
python verify_startup.py
```

## 📁 Key Directories

- `backend/uploads/` - Uploaded resume files
- `backend/job_application.db` - SQLite database

## 🔧 First-Time Setup

### Backend (One-time)
```bash
cd backend
pip install -r requirements.txt
python -m app.database.init_db
```

### Frontend (One-time)
```bash
cd frontend
npm install
```

## 🐛 Troubleshooting

**Backend won't start?**
- Check: `python --version` (need 3.12+)
- Run: `pip install -r requirements.txt`

**Frontend won't start?**
- Check: `node --version` (need 20+)
- Run: `npm install`

**Database errors?**
- Run: `python -m app.database.init_db` in backend directory

## 📋 Features Implemented

✅ Resume Upload (PDF only, max 5MB)
✅ Resume List with delete
✅ Database persistence
✅ File storage
✅ Full API documentation

## 🎯 Next Steps

1. Open http://localhost:3000
2. Click "Upload Resume"
3. Upload a PDF file
4. View uploaded resumes in the list
5. Test delete functionality
