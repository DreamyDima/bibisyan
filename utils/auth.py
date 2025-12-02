import hashlib, time
from redis_client import redis_db

SESSION_EXPIRATION = 1800  # 30 minutes

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password: str, stored_hash: str):
    return hashlib.sha256(password.encode()).hexdigest() == stored_hash

def is_admin_logged_in(user_id: int) -> bool:
    return redis_db.get(f"admin_session:{user_id}") == "1"

def start_admin_session(user_id: int):
    redis_db.setex(f"admin_session:{user_id}", SESSION_EXPIRATION, "1")

def end_admin_session(user_id: int):
    redis_db.delete(f"admin_session:{user_id}")