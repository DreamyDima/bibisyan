"""
Redis client initialization with error handling.
"""

import logging
import os
import redis
from redis.exceptions import RedisError

logger = logging.getLogger(__name__)

# Get Redis configuration from environment variables
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
    # Test connection
    redis_db.ping()
    logger.info("Redis connection established successfully")
except RedisError as e:
    logger.error(f"Failed to connect to Redis: {e}")
    raise