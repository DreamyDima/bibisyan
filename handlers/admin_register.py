from aiogram import Router, types
from database.engine import SessionLocal
from database.models import Admin
from utils.auth import hash_password
from config import OWNER_ID

router = Router()

@router.message(commands=["addadmin"])
async def add_admin(m: types.Message):
    if m.from_user.id != OWNER_ID:
        return
    
    try:
        _, user_id, password = m.text.split()
        user_id = int(user_id)
    except:
        await m.reply("Usage:\n/addadmin USER_ID PASSWORD")
        return

    with SessionLocal.begin() as s:
        a = Admin(
            user_id=user_id,
            username=None,
            password_hash=hash_password(password)
        )
        s.add(a)

    await m.reply(f"Added admin {user_id}.")