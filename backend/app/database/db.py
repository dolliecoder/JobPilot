import logging
import traceback
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./job_application.db")
logger.info(f"DATABASE_URL loaded, prefix={DATABASE_URL.split('://')[0] if '://' in DATABASE_URL else 'unknown'}")

try:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
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
