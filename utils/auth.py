"""
Authentication utilities for admin access and session management.
"""

import logging
import bcrypt
from redis_client import redis_db
from config import ADMIN_SESSION_EXPIRATION

logger = logging.getLogger(__name__)


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt with a salt.
    
    Args:
        password: The plaintext password to hash.
    
    Returns:
        The bcrypt hash of the password.
    """
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode(), salt).decode()


def check_password(password: str, stored_hash: str) -> bool:
    """
    Check if a plaintext password matches a bcrypt hash.
    
    Args:
        password: The plaintext password to check.
        stored_hash: The bcrypt hash to compare against.
    
    Returns:
        True if the password matches, False otherwise.
    """
    try:
        return bcrypt.checkpw(password.encode(), stored_hash.encode())
    except Exception as e:
        logger.error(f"Error checking password: {e}")
        return False


def is_admin_logged_in(user_id: int) -> bool:
    """
    Check if an admin user has an active session.
    
    Args:
        user_id: The Telegram user ID.
    
    Returns:
        True if the user has an active admin session, False otherwise.
    """
    try:
        return redis_db.get(f"admin_session:{user_id}") == "1"
    except Exception as e:
        logger.error(f"Error checking admin session: {e}")
        return False


def start_admin_session(user_id: int) -> None:
    """
    Create a new admin session for a user.
    
    Args:
        user_id: The Telegram user ID.
    """
    try:
        redis_db.setex(f"admin_session:{user_id}", ADMIN_SESSION_EXPIRATION, "1")
        logger.info(f"Admin session started for user {user_id}")
    except Exception as e:
        logger.error(f"Error starting admin session: {e}")


def end_admin_session(user_id: int) -> None:
    """
    End an active admin session for a user.
    
    Args:
        user_id: The Telegram user ID.
    """
    try:
        redis_db.delete(f"admin_session:{user_id}")
        logger.info(f"Admin session ended for user {user_id}")
    except Exception as e:
        logger.error(f"Error ending admin session: {e}")