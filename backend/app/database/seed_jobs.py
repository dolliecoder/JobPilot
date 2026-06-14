"""
Seed sample jobs into the database
Run this script to populate the database with sample job postings
"""

from app.database.db import SessionLocal
from app.models.job import Job
from datetime import datetime, timedelta
import random

def seed_jobs():
    """Seed the database with sample job postings"""
    db = SessionLocal()
    
    # Check if jobs already exist
    existing_jobs = db.query(Job).count()
    if existing_jobs > 0:
        print(f"Database already has {existing_jobs} jobs. Skipping seed.")
        db.close()
        return
    
    sample_jobs = [
        {
            "title": "Java Developer",
            "company": "Tech Solutions Inc",
            "location": "New York, NY",
            "job_type": "Full-time",
            "description": "We are looking for an experienced Java Developer to join our backend team. You will be responsible for building high-performance applications.",
            "requirements": "5+ years Java experience, Spring Boot, Microservices, REST APIs"
        },
        {
            "title": "Full Stack Developer",
            "company": "Digital Innovations Ltd",
            "location": "San Francisco, CA",
            "job_type": "Full-time",
            "description": "Join our team as a Full Stack Developer working on cutting-edge web applications using modern technologies.",
            "requirements": "React, Node.js, PostgreSQL, AWS, 3+ years experience"
        },
        {
            "title": "Python Developer",
            "company": "Data Systems Corp",
            "location": "Austin, TX",
            "job_type": "Full-time",
            "description": "Seeking a Python Developer to work on data processing pipelines and machine learning applications.",
            "requirements": "Python, Django/Flask, SQL, pandas, scikit-learn"
        },
        {
            "title": ".NET Developer",
            "company": "Enterprise Software Group",
            "location": "Chicago, IL",
            "job_type": "Full-time",
            "description": "We need a .NET Developer to maintain and enhance our enterprise applications built on the Microsoft stack.",
            "requirements": "C#, .NET Core, ASP.NET, SQL Server, Azure"
        },
        {
            "title": "React Developer",
            "company": "UI/UX Studios",
            "location": "Seattle, WA",
            "job_type": "Full-time",
            "description": "Looking for a talented React Developer to create beautiful, responsive user interfaces for our clients.",
            "requirements": "React, TypeScript, Redux, CSS3, Jest, 2+ years experience"
        },
        {
            "title": "Senior Java Engineer",
            "company": "Financial Tech Solutions",
            "location": "Boston, MA",
            "job_type": "Full-time",
            "description": "Senior Java Engineer needed for developing high-frequency trading systems and financial applications.",
            "requirements": "7+ years Java, Spring Framework, Kafka, Redis, distributed systems"
        },
        {
            "title": "Full Stack JavaScript Developer",
            "company": "Startup Ventures",
            "location": "Remote",
            "job_type": "Contract",
            "description": "Join our startup as a Full Stack JavaScript Developer and help build our MVP from the ground up.",
            "requirements": "Node.js, Express, React, MongoDB, Git"
        },
        {
            "title": "Python Data Engineer",
            "company": "Analytics Pro",
            "location": "Denver, CO",
            "job_type": "Full-time",
            "description": "Python Data Engineer to design and implement data pipelines for our analytics platform.",
            "requirements": "Python, Apache Spark, Airflow, SQL, AWS/GCP"
        },
        {
            "title": "Lead .NET Architect",
            "company": "Cloud Services Inc",
            "location": "Dallas, TX",
            "job_type": "Full-time",
            "description": "Lead .NET Architect position to design scalable cloud-native applications on Azure.",
            "requirements": "10+ years .NET, Azure, microservices architecture, leadership experience"
        },
        {
            "title": "Frontend React Developer",
            "company": "E-commerce Giants",
            "location": "Los Angeles, CA",
            "job_type": "Full-time",
            "description": "Frontend Developer specializing in React to build our next-generation e-commerce platform.",
            "requirements": "React, Next.js, TypeScript, TailwindCSS, performance optimization"
        },
        {
            "title": "Java Spring Boot Developer",
            "company": "Healthcare Systems",
            "location": "Philadelphia, PA",
            "job_type": "Full-time",
            "description": "Java Spring Boot Developer for building HIPAA-compliant healthcare management systems.",
            "requirements": "Java, Spring Boot, Security, REST APIs, healthcare domain knowledge"
        },
        {
            "title": "Full Stack MERN Developer",
            "company": "Social Media Startup",
            "location": "Miami, FL",
            "job_type": "Part-time",
            "description": "Part-time Full Stack MERN Developer to build features for our growing social media platform.",
            "requirements": "MongoDB, Express, React, Node.js, Socket.io"
        },
        {
            "title": "Python Machine Learning Engineer",
            "company": "AI Research Labs",
            "location": "San Jose, CA",
            "job_type": "Full-time",
            "description": "ML Engineer to develop and deploy machine learning models for production systems.",
            "requirements": "Python, TensorFlow/PyTorch, MLOps, Docker, Kubernetes"
        },
        {
            "title": ".NET Core Developer",
            "company": "Banking Solutions",
            "location": "Charlotte, NC",
            "job_type": "Full-time",
            "description": ".NET Core Developer for building secure banking applications and payment processing systems.",
            "requirements": ".NET Core, C#, Entity Framework, SQL Server, security best practices"
        },
        {
            "title": "React Native Mobile Developer",
            "company": "Mobile Apps Co",
            "location": "Portland, OR",
            "job_type": "Contract",
            "description": "React Native Developer to build cross-platform mobile applications for iOS and Android.",
            "requirements": "React Native, JavaScript, iOS/Android development, REST APIs"
        }
    ]
    
    print(f"Seeding {len(sample_jobs)} jobs into the database...")
    
    for i, job_data in enumerate(sample_jobs):
        # Create jobs with varying created dates (within last 30 days)
        days_ago = random.randint(0, 30)
        job = Job(**job_data)
        db.add(job)
    
    db.commit()
    print(f"✅ Successfully seeded {len(sample_jobs)} jobs!")
    db.close()

if __name__ == "__main__":
    seed_jobs()
