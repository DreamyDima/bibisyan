from aiogram import types, Router
from database.engine import SessionLocal
from database.models import UserCard, Card
from keyboards.inventory_kb import inventory_card_kb

router = Router()

@router.message(commands=["inventory"])
async def inventory(m: types.Message):
    uid = m.from_user.id

    with SessionLocal() as s:
        rows = (
            s.query(UserCard, Card)
            .join(Card, UserCard.card_id == Card.id)
            .filter(UserCard.user_id == uid)
            .all()
        )

    if not rows:
        await m.reply("Your inventory is empty.")
        return

    for uc, card in rows:
        await m.answer_photo(
            photo=card.image_file_id,
            caption=f"{card.name} (qty: {uc.qty})",
            reply_markup=inventory_card_kb(card.id)
        )