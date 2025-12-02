from aiogram import Router, types
from utils.auth import is_admin_logged_in
from utils.admin_logger import admin_log

router = Router()

@router.message(commands=["adminpanel"])
async def admin_panel(m: types.Message):
    uid = m.from_user.id

    if not is_admin_logged_in(uid):
        await m.reply("🔒 You must login first.\nUse /adminlogin")
        return

    await m.reply(
        "⚙️ Admin Panel:\n"
        "/addcard – add card\n"
        "/viewlogs – show logs\n"
        "/proposals – pending proposals"
    )

    await admin_log(
        m.bot, uid,
        "admin_panel_opened",
        "Accessed admin panel"
    )