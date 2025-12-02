"""
Redis client initialization with error handling.
Supports both direct configuration and Railway REDIS_URL.
"""

import logging
import os
import redis
from redis.exceptions import RedisError

logger = logging.getLogger(__name__)

# Check for Railway REDIS_URL (takes precedence)
redis_url = os.getenv("REDIS_URL")

if redis_url:
    # Railway provides REDIS_URL in format: redis://user:password@host:port
    try:
        redis_db = redis.from_url(
            redis_url,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_keepalive=True,
        )
        redis_db.ping()
        logger.info("Redis connection established from REDIS_URL")
    except RedisError as e:
        logger.error(f"Failed to connect to Redis via REDIS_URL: {e}")
        raise
else:
    # Fallback to individual configuration (local development)
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_DB = int(os.getenv("REDIS_DB", "0"))

    try:
        redis_db = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True,
            socket_connect_timeout=5,
            socket_keepalive=True,
        )
        redis_db.ping()
        logger.info("Redis connection established from local config")
    except RedisError as e:
        logger.error(f"Failed to connect to Redis: {e}")
        raise