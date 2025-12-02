import random
from aiogram import types, Router
from database.engine import SessionLocal
from utils.cooldown import can_drop, set_cooldown
from utils.helper import choose_random_card
from config import DROP_CHANCE_PER_MSG
from database.models import Drop
from bot import bot

router = Router()

@router.message()
async def group_drop_trigger(m: types.Message):
    if m.chat.type not in ("group", "supergroup"):
        return
    
    uid = m.from_user.id

    # Each player has their own cooldown
    if not can_drop(uid):
        return

    if random.random() > DROP_CHANCE_PER_MSG:
        return

    with SessionLocal() as s:
        card = choose_random_card(s)
        if not card:
            return

        msg = await bot.send_photo(
            chat_id=m.chat.id,
            photo=card.image_file_id,
            caption=f"Drop! {card.name}\nRarity: {card.rarity}",
            reply_markup=None  # claim is separate
        )

        drop = Drop(message_id=msg.message_id, chat_id=m.chat.id, card_id=card.id)
        s.add(drop)
        s.commit()

    set_cooldown(uid)