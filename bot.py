"""
Main bot entry point for the Telegram bot application.
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import (
    drops,
    claims,
    profile,
    inventory,
    leaderboard,
    admin_add_card,
    proposals,
    natural_commands,
    admin_login,
    admin_panel,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Register all routers
dp.include_router(drops.router)
dp.include_router(claims.router)
dp.include_router(profile.router)
dp.include_router(inventory.router)
dp.include_router(leaderboard.router)
dp.include_router(natural_commands.router)
dp.include_router(admin_add_card.router)
dp.include_router(proposals.router)
dp.include_router(admin_login.router)
dp.include_router(admin_panel.router)


async def main() -> None:
    """Start the bot polling."""
    logger.info("Starting bot polling...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error during polling: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
