import logging
import traceback
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./job_application.db")

# Log the database type being used (mask credentials for Postgres)
db_prefix = DATABASE_URL.split("://")[0] if "://" in DATABASE_URL else "unknown"
logger.info(f"DATABASE_URL loaded, scheme={db_prefix}")

# If using SQLite default, use an absolute path to avoid CWD surprises
if "sqlite" in db_prefix:
    db_path = DATABASE_URL.replace("sqlite:///", "")
    if not os.path.isabs(db_path):
        abs_path = os.path.abspath(db_path)
        DATABASE_URL = f"sqlite:///{abs_path}"
        logger.info(f"Resolved SQLite path to: {abs_path}")

try:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False} if "sqlite" in db_prefix else {}
    )
    logger.info("Engine created, testing connection...")
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        logger.info("Database engine connection test OK")
except Exception as e:
    logger.error(f"Engine creation failed: {type(e).__name__}: {e}")
    logger.error(traceback.format_exc())
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db_tables():
    """Create all database tables and return list of created tables."""
    try:
        logger.info("Creating database tables...")
        if "sqlite" in db_prefix:
            db_dir = os.path.dirname(
                DATABASE_URL.replace("sqlite:///", "")
            )
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir, exist_ok=True)
                logger.info(f"Created database directory: {db_dir}")

        Base.metadata.create_all(bind=engine)

        # Verify tables were created
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        logger.info(f"Tables after create_all: {existing_tables}")

        expected_tables = {"jobs", "resumes", "applications"}
        missing = expected_tables - set(existing_tables)
        if missing:
            logger.warning(f"Missing tables after create_all: {missing}")
        else:
            logger.info("All expected tables exist")
        return existing_tables
    except Exception as e:
        logger.error(f"Table creation failed: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        raise


def seed_jobs_if_empty(db_session):
    """Seed sample jobs if the jobs table is empty."""
    from app.models.job import Job

    try:
        count = db_session.query(Job).count()
        logger.info(f"Current job count: {count}")
        if count > 0:
            logger.info("Jobs already exist, skipping seed")
            return

        logger.info("Seeding sample jobs...")
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
            },
        ]

        for job_data in sample_jobs:
            db_session.add(Job(**job_data))
        db_session.commit()
        logger.info(f"Seeded {len(sample_jobs)} sample jobs successfully")
    except Exception as e:
        db_session.rollback()
        logger.error(f"Job seeding failed: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        raise


def get_db():
    """Dependency for database session"""
    db = None
    try:
        logger.info("Creating new database session...")
        db = SessionLocal()
        logger.info(f"Session created: {db}")
        yield db
    except Exception as e:
        logger.error(f"Database session error: {type(e).__name__}: {e}")
        logger.error(traceback.format_exc())
        raise
    finally:
        if db is not None:
            logger.info("Closing database session")
            db.close()
