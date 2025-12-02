"""
Drop handler for randomly dropping cards in group chats.
"""

import logging
import random
from aiogram import types, Router
from database.engine import SessionLocal
from utils.cooldown import can_drop, set_cooldown
from utils.helper import choose_random_card
from config import DROP_CHANCE_PER_MSG
from database.models import Drop
from bot import bot

logger = logging.getLogger(__name__)

router = Router()


@router.message()
async def group_drop_trigger(m: types.Message) -> None:
    """
    Trigger a random card drop in group chats.
    
    Args:
        m: The message that triggered this handler.
    """
    try:
        # Only trigger in group or supergroup chats
        if m.chat.type not in ("group", "supergroup"):
            return
        
        uid = m.from_user.id

        # Check if user is on cooldown
        if not can_drop(uid):
            return

        # Random chance to trigger a drop
        if random.random() > DROP_CHANCE_PER_MSG:
            return

        # Get a random card from the database
        with SessionLocal() as s:
            card = choose_random_card(s)
            if not card:
                logger.warning("No card available for drop")
                return

            # Send the card to the group
            msg = await bot.send_photo(
                chat_id=m.chat.id,
                photo=card.image_file_id,
                caption=f"Drop! {card.name}\nRarity: {card.rarity}",
            )

            # Record the drop in the database
            drop = Drop(
                message_id=msg.message_id,
                chat_id=m.chat.id,
                card_id=card.id
            )
            s.add(drop)
            s.commit()
            logger.info(f"Drop created: card {card.id} in chat {m.chat.id}")

        # Set cooldown for the user
        set_cooldown(uid)
        
    except Exception as e:
        logger.error(f"Error in group_drop_trigger: {e}")