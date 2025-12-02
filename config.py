TOKEN = "7971006276:AAE5UiLXDdHhvLuTu9AeHZOLJRGlZF3TXkw"

# Owner can add cards from Telegram
OWNER_ID = 123456789  

from utils.auth import is_admin_logged_in

if not is_admin_logged_in(m.from_user.id):
    await m.reply("🔒 You must login first.")
    return
  
# Drop cooldown: 1 hour
DROP_COOLDOWN_SECONDS = 3600

# Random drop chance per message
DROP_CHANCE_PER_MSG = 0.005