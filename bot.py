import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import drops, claims, profile, inventory, leaderboard

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Register routers
dp.include_router(drops.router)
dp.include_router(claims.router)
dp.include_router(profile.router)
dp.include_router(inventory.router)
dp.include_router(leaderboard.router)
from handlers import admin_add_card, proposals, natural_commands

dp.include_router(natural_commands.router)
dp.include_router(admin_add_card.router)
dp.include_router(proposals.router)

from handlers import admin_login, admin_panel

dp.include_router(admin_login.router)
dp.include_router(admin_panel.router)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
from handlers import admin_add_card, proposals, natural_commands
