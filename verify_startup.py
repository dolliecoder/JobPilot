#!/usr/bin/env python3
"""
Startup Verification Script for AI Job Application System
Run this script to verify both backend and frontend are running correctly.
"""

import requests
import sys
from time import sleep

def check_backend():
    """Check if backend is running and responding"""
    print("🔍 Checking Backend...")
    try:
        # Check health endpoint
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200 and response.json().get("status") == "healthy":
            print("✅ Backend is running and healthy")
            
            # Check API root
            response = requests.get("http://localhost:8000/", timeout=5)
            if response.status_code == 200:
                print("✅ API root endpoint is accessible")
                
            # Check resumes endpoint
            response = requests.get("http://localhost:8000/api/resumes/", timeout=5)
            if response.status_code == 200:
                print("✅ Resumes API endpoint is working")
                
            # Check docs
            response = requests.get("http://localhost:8000/docs", timeout=5)
            if response.status_code == 200:
                print("✅ API documentation is accessible at http://localhost:8000/docs")
                
            return True
        else:
            print("❌ Backend health check failed")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running on http://localhost:8000")
        print("   Start it with: cd backend && python -m uvicorn app.main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error checking backend: {e}")
        return False

def check_frontend():
    """Check if frontend is running and responding"""
    print("\n🔍 Checking Frontend...")
    try:
        response = requests.get("http://localhost:3000/", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is running on http://localhost:3000")
            return True
        else:
            print(f"❌ Frontend returned status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Frontend is not running on http://localhost:3000")
        print("   Start it with: cd frontend && npm run dev")
        return False
    except Exception as e:
        print(f"❌ Error checking frontend: {e}")
        return False

def check_database():
    """Check if database file exists"""
    print("\n🔍 Checking Database...")
    import os
    db_path = "backend/job_application.db"
    if os.path.exists(db_path):
        size = os.path.getsize(db_path)
        print(f"✅ Database file exists ({size} bytes)")
        return True
    else:
        print("❌ Database file not found")
        print("   Initialize it with: cd backend && python -m app.database.init_db")
        return False

def check_uploads_dir():
    """Check if uploads directory exists"""
    print("\n🔍 Checking Uploads Directory...")
    import os
    uploads_path = "backend/uploads"
    if os.path.exists(uploads_path) and os.path.isdir(uploads_path):
        print("✅ Uploads directory exists")
        return True
    else:
        print("❌ Uploads directory not found")
        return False

def main():
    print("=" * 60)
    print("AI Job Application System - Startup Verification")
    print("=" * 60)
    
    results = []
    
    # Check all components
    results.append(("Backend", check_backend()))
    results.append(("Frontend", check_frontend()))
    results.append(("Database", check_database()))
    results.append(("Uploads Directory", check_uploads_dir()))
    
    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)
    
    all_passed = all(result[1] for result in results)
    
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{name:20s}: {status}")
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All checks passed! System is ready to use.")
        print("\n📍 URLs:")
        print("   Frontend: http://localhost:3000")
        print("   Backend:  http://localhost:8000")
        print("   API Docs: http://localhost:8000/docs")
        return 0
    else:
        print("\n⚠️  Some checks failed. Please review the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
