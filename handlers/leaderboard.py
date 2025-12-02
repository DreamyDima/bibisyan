from aiogram import types, Router
from database.engine import SessionLocal
from database.models import User

router = Router()

@router.message(commands=["leaderboard"])
async def leaderboard(m: types.Message):
    with SessionLocal() as s:
        top = s.query(User).order_by(User.points.desc()).limit(10).all()

    if not top:
        await m.reply("No data.")
        return

    lines = []
    for i, u in enumerate(top, 1):
        lines.append(f"{i}. {u.username or u.id} — {u.points} pts")

    await m.reply("\n".join(lines))