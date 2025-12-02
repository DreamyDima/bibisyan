"""
Database engine and session configuration.
"""

import logging
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)

# Get database URL from environment variables
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/bot_db"
)

try:
    # Create engine with connection pooling
    engine = create_engine(
        DATABASE_URL,
        pool_size=10,
        max_overflow=20,
        echo=False,
        pool_pre_ping=True,  # Test connections before using them
    )
    logger.info("Database engine created successfully")
except SQLAlchemyError as e:
    logger.error(f"Failed to create database engine: {e}")
    raise

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)