"""
Cooldown management utilities for drop functionality.
"""

import logging
from redis_client import redis_db
from config import DROP_COOLDOWN_SECONDS

logger = logging.getLogger(__name__)


def can_drop(user_id: int) -> bool:
    """
    Check if a user can perform a drop action (cooldown has expired).
    
    Args:
        user_id: The user's ID.
    
    Returns:
        True if the user can drop, False if they are on cooldown.
    """
    try:
        return redis_db.get(f"cooldown:{user_id}") is None
    except Exception as e:
        logger.error(f"Error checking cooldown for user {user_id}: {e}")
        return False


def set_cooldown(user_id: int) -> None:
    """
    Set a cooldown for a user after they perform a drop.
    
    Args:
        user_id: The user's ID.
    """
    try:
        redis_db.setex(f"cooldown:{user_id}", DROP_COOLDOWN_SECONDS, "1")
        logger.debug(f"Cooldown set for user {user_id}")
    except Exception as e:
        logger.error(f"Error setting cooldown for user {user_id}: {e}")