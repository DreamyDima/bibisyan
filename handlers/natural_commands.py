from aiogram import types, Router
from aiogram.filters import Text

router = Router()

INVENTORY_WORDS = ["inventory", "inv", "bag", "my cards", "cards"]
PROFILE_WORDS = ["profile", "stats", "my profile", "me"]
LEADERBOARD_WORDS = ["leaderboard", "top", "ranking"]

@router.message()
async def natural_parser(m: types.Message):
    text = m.text.lower()

    if text in INVENTORY_WORDS:
        await m.bot.send_message(m.chat.id, "/inventory")
        return

    if text in PROFILE_WORDS:
        await m.bot.send_message(m.chat.id, "/profile")
        return

    if text in LEADERBOARD_WORDS:
        await m.bot.send_message(m.chat.id, "/leaderboard")
        return