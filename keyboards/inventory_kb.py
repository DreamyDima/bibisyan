from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def inventory_card_kb(card_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Set Favorite", callback_data=f"fav:{card_id}")],
        [InlineKeyboardButton(text="ℹ View Details", callback_data=f"info:{card_id}")]
    ])