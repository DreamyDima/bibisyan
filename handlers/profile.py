from aiogram import types, Router
from database.engine import SessionLocal
from database.models import User, Card

router = Router()

@router.message(commands=["profile"])
async def profile(m: types.Message):
    uid = m.from_user.id

    with SessionLocal() as s:
        user = s.get(User, uid)
        if not user:
            await m.reply("No profile found.")
            return

        fav = s.get(Card, user.favorite_card_id)
        fav_name = fav.name if fav else "None"

        txt = (
            f"👤 {user.username}\n"
            f"⭐ Favorite: {fav_name}\n"
            f"🪙 Coins: {user.coins}\n"
            f"💠 Points: {user.points}"
        )

        await m.reply(txt)