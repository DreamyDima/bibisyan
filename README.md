# Bibisyan - Telegram Card Collection Bot

A feature-rich Telegram bot for collecting and trading digital cards in group chats. Players can receive random card drops, manage their inventory, and compete on leaderboards.

## Features

- **Random Card Drops**: Cards are randomly dropped in group chats with configurable rarity and frequency
- **Inventory Management**: Users can view and manage their card collections
- **Leaderboards**: Track top users by points or coins
- **User Profiles**: Display user statistics and favorite cards
- **Admin Panel**: Administrative interface for managing cards and users
- **Authentication**: Secure admin login with bcrypt password hashing
- **Session Management**: Redis-based admin session management

## Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Redis 6+
- Telegram Bot API token (from BotFather)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd bibisyan
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` with your settings:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   OWNER_ID=your_telegram_id
   DATABASE_URL=postgresql://user:password@localhost:5432/bot_db
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```

5. **Initialize the database**:
   ```bash
   python init_db.py
   ```

6. **Run the bot**:
   ```bash
   python bot.py
   ```

## Project Structure

```
├── bot.py                 # Main bot entry point
├── config.py             # Configuration from environment variables
├── redis_client.py       # Redis connection
├── init_db.py            # Database initialization script
├── database/
│   ├── engine.py         # SQLAlchemy engine and session
│   ├── models.py         # Database models
│   └── __init__.py
├── handlers/             # Bot command handlers
│   ├── drops.py          # Card drop logic
│   ├── claims.py         # Card claiming logic
│   ├── inventory.py      # Inventory management
│   ├── profile.py        # User profiles
│   ├── leaderboard.py    # Leaderboard functionality
│   ├── admin_login.py    # Admin authentication
│   ├── admin_panel.py    # Admin management interface
│   ├── admin_add_card.py # Add new cards
│   ├── admin_register.py # Register new admins
│   ├── proposals.py      # User proposals
│   ├── natural_commands.py # Natural language processing
│   └── __init__.py
├── keyboards/            # Telegram keyboard layouts
│   ├── inventory_kb.py
│   └── __init__.py
├── utils/                # Utility functions
│   ├── auth.py           # Authentication utilities
│   ├── cooldown.py       # Cooldown management
│   ├── helper.py         # Helper functions
│   ├── rarity.py         # Rarity calculations
│   └── __init__.py
├── logs/                 # Application logs
├── requirements.txt      # Project dependencies
├── .env.example          # Environment variables template
└── .gitignore           # Git ignore configuration
```

## Configuration

### Environment Variables

Key configuration options in `.env`:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from BotFather
- `OWNER_ID`: Telegram ID of the bot owner
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_HOST`: Redis server hostname
- `REDIS_PORT`: Redis server port
- `REDIS_DB`: Redis database number
- `DROP_COOLDOWN_SECONDS`: Cooldown between drops for each user (default: 3600)
- `DROP_CHANCE_PER_MSG`: Probability of drop per message (default: 0.005)
- `ADMIN_SESSION_EXPIRATION`: Admin session timeout in seconds (default: 1800)

## Usage

### User Commands

- `/start` - Start using the bot
- `/profile` - View your profile
- `/inventory` - View your card collection
- `/leaderboard` - View top users

### Admin Commands

- `/adminlogin` - Login as admin
- `/adminlogout` - Logout from admin mode
- `/addcard` - Add a new card
- `/register` - Register a new admin

## Database

The bot uses PostgreSQL with SQLAlchemy ORM. Key models:

- **User**: Telegram users with their stats
- **Card**: Collectible cards with rarity levels
- **UserCard**: Inventory items (user-card associations)
- **Drop**: Record of card drops in chats
- **Admin**: Administrator accounts

## Security

- Bot tokens and database credentials are stored in `.env` (not versioned)
- Admin passwords are hashed using bcrypt with salt
- Admin sessions are managed via Redis with expiration
- Database connections use connection pooling
- Input validation and error handling throughout

## Dependencies

- **aiogram**: Telegram bot framework
- **sqlalchemy**: ORM for database management
- **psycopg2**: PostgreSQL adapter
- **redis**: Redis client
- **bcrypt**: Secure password hashing
- **python-dotenv**: Environment variable management

## Development

### Code Quality

- Type hints on all functions
- Comprehensive docstrings
- Structured error handling
- Logging for debugging

### Code Style

The project follows PEP 8 guidelines.

## Troubleshooting

### Redis Connection Error
- Ensure Redis is running: `redis-cli ping`
- Check Redis configuration in `.env`

### Database Connection Error
- Verify PostgreSQL is running
- Check DATABASE_URL in `.env`
- Ensure database exists

### Bot Not Responding
- Check TELEGRAM_BOT_TOKEN in `.env`
- Review logs for errors
- Ensure bot has proper permissions

## License

This project is open source. See LICENSE file for details.

## Support

For issues and feature requests, please open an issue on the repository.