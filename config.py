import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Configuration
TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
OWNER_ID: int = int(os.getenv("OWNER_ID", "123456789"))

# Drop Configuration
DROP_COOLDOWN_SECONDS: int = int(os.getenv("DROP_COOLDOWN_SECONDS", "3600"))
DROP_CHANCE_PER_MSG: float = float(os.getenv("DROP_CHANCE_PER_MSG", "0.005"))

# Admin Configuration
ADMIN_SESSION_EXPIRATION: int = int(os.getenv("ADMIN_SESSION_EXPIRATION", "1800"))

# Validate critical configuration
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set")