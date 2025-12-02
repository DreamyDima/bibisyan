from redis_client import redis_db
from config import DROP_COOLDOWN_SECONDS

def can_drop(user_id: int) -> bool:
    return redis_db.get(f"cooldown:{user_id}") is None

def set_cooldown(user_id: int):
    redis_db.setex(f"cooldown:{user_id}", DROP_COOLDOWN_SECONDS, "1")