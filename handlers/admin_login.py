from aiogram import Router, types
from database.engine import SessionLocal
from database.models import Admin
from utils.auth import check_password, start_admin_session, end_admin_session, is_admin_logged_in
from utils.admin_logger import admin_log

router = Router()
state = {}

@router.message(commands=["adminlogin"])
async def admin_login_cmd(m: types.Message):
    state[m.from_user.id] = "awaiting_password"
    await m.reply("🔐 Enter admin password:")

@router.message()
async def admin_login_flow(m: types.Message):
    uid = m.from_user.id
    if uid not in state:
        return

    if state[uid] != "awaiting_password":
        return

    password = m.text

    with SessionLocal() as s:
        admin = s.query(Admin).filter_by(user_id=uid).first()

        if not admin:
            await m.reply("❌ You are not registered as an admin.")
            del state[uid]
            return

        if not check_password(password, admin.password_hash):
            await m.reply("❌ Wrong password.")
            del state[uid]
            return

    start_admin_session(uid)
    await m.reply("✅ Login successful.\nWelcome to admin mode.")

    await admin_log(
        m.bot, uid,
        "admin_login",
        f"Admin {uid} logged in"
    )

    del state[uid]

@router.message(commands=["adminlogout"])
async def admin_logout(m: types.Message):
    uid = m.from_user.id

    if not is_admin_logged_in(uid):
        await m.reply("You are not logged in.")
        return

    end_admin_session(uid)
    await m.reply("🔒 Logged out successfully.")

    await admin_log(
        m.bot, uid,
        "admin_logout",
        f"Admin {uid} logged out"
    )