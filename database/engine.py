"""
Database engine and session configuration.
Supports both local PostgreSQL and Railway DATABASE_URL.
"""

import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)

# Get database URL from environment variables
# Railway provides DATABASE_URL, local development uses separate components
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/bot_db"
)

# Railway uses postgresql:// URL format, ensure it's compatible
if DATABASE_URL.startswith("postgresql://"):
    # Already in correct format
    db_url = DATABASE_URL
else:
    # Fallback for custom format (shouldn't happen with Railway)
    db_url = DATABASE_URL

try:
    # Create engine with connection pooling
    # Railway uses connection pooling limits, so set reasonable values
    engine = create_engine(
        db_url,
        pool_size=5,  # Reduced for Railway's constraints
        max_overflow=10,
        echo=False,
        pool_pre_ping=True,  # Test connections before using them
        pool_recycle=3600,  # Recycle connections every hour
    )
    logger.info("Database engine created successfully")
except SQLAlchemyError as e:
    logger.error(f"Failed to create database engine: {e}")
    raise

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)