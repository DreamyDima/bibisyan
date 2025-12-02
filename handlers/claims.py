from aiogram import types, Router
from database.engine import SessionLocal
from database.models import Drop, User, UserCard, Card

router = Router()

@router.callback_query(lambda c: c.data.startswith("claim:"))
async def claim_card(callback: types.CallbackQuery):
    _, card_id = callback.data.split(":")
    card_id = int(card_id)
    chat_id = callback.message.chat.id
    msg_id = callback.message.message_id
    uid = callback.from_user.id

    with SessionLocal.begin() as s:
        drop = (
            s.query(Drop)
            .filter_by(message_id=msg_id, chat_id=chat_id, card_id=card_id)
            .with_for_update()
            .first()
        )

        if not drop or drop.claimed_by:
            await callback.answer("Already claimed.")
            return

        user = s.get(User, uid) or User(id=uid, username=callback.from_user.username)
        if not user.id:
            s.add(user)
            s.flush()

        card = s.get(Card, card_id)

        owned = s.query(UserCard).filter_by(user_id=uid, card_id=card_id).first()

        if not owned:
            owned = UserCard(user_id=uid, card_id=card_id, qty=1)
            s.add(owned)
        else:
            # Only points/coins after first time
            pass

        user.points += card.points
        user.coins += card.coins

        drop.claimed_by = uid

    await callback.answer("You claimed it!")