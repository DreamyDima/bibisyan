# Railway Deployment Guide

## Quick Deploy Steps

### 1. Prerequisites
- GitHub account with this repository pushed
- Railway account (sign up at railway.app)
- Telegram Bot token from BotFather

### 2. Create Railway Project

```bash
# Install Railway CLI (optional, but helpful)
npm install -g @railway/cli

# Or login via web at railway.app
```

### 3. Connect GitHub Repository

1. Go to railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Authorize Railway with GitHub
5. Select the `bibisyan` repository
6. Click "Deploy"

### 4. Add PostgreSQL Database

1. In your Railway project, click "+ Add"
2. Select "Database" → "PostgreSQL"
3. Wait for provisioning (1-2 minutes)
4. Railway auto-creates `DATABASE_URL` variable

### 5. Add Redis Cache

1. Click "+ Add" again
2. Select "Database" → "Redis"
3. Wait for provisioning
4. Railway auto-creates `REDIS_URL` variable

### 6. Configure Environment Variables

In your Railway project's Variables tab, add:

```
TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
OWNER_ID=your_telegram_user_id
DROP_COOLDOWN_SECONDS=3600
DROP_CHANCE_PER_MSG=0.005
ADMIN_SESSION_EXPIRATION=1800
PYTHONUNBUFFERED=1
```

### 7. Deploy

Push to GitHub and Railway will auto-deploy:

```bash
git add Procfile
git commit -m "Add Railway Procfile and update for Railway compatibility"
git push origin main
```

### 8. Monitor Deployment

1. Go to "Deployments" tab in Railway
2. Click the latest deployment
3. View "Logs" to see:
   ```
   Starting bot polling...
   ```

### 9. Initialize Database

#### Option A: Using Railway Shell
1. Click your deployment
2. Go to "Shell"
3. Run:
   ```bash
   source venv/bin/activate
   python init_db.py
   ```

#### Option B: Using Railway CLI
```bash
railway shell
python init_db.py
```

### 10. Test the Bot

Send a message to your Telegram bot. It should respond if connected properly.

## Troubleshooting

### Bot not responding
1. Check logs: Deployments → View logs
2. Verify `TELEGRAM_BOT_TOKEN` is set correctly
3. Check bot is marked as running in Telegram BotFather

### Database connection error
```bash
railway shell
python -c "from database.engine import engine; print(engine.connect())"
```

### Redis connection error
```bash
railway shell
python -c "from redis_client import redis_db; print(redis_db.ping())"
```

### View all environment variables
```bash
railway shell
env | grep -E "(DATABASE|REDIS|TELEGRAM)"
```

## Important Notes

### Railway Pricing
- Free tier includes: 5GB storage, limited compute hours
- Usage pricing for larger deployments
- PostgreSQL and Redis included in free tier

### Dyno Types
- `worker`: Background task (what we use for the bot)
- `web`: Web server (not needed for telegram bot)

### Auto-Deploy
- Railway auto-deploys when you push to GitHub
- Check deployment status in Railway dashboard

### Keep-Alive
- Railway puts workers to sleep after 30 minutes of inactivity
- Consider upgrading to paid for always-on workers
- Or use Railway's scheduled tasks to wake up periodically

## Environment Variables Set by Railway

These are automatically provided:
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `PORT`: (for web apps, not needed for worker)

## File Changes for Railway

Files modified for Railway compatibility:
- `Procfile` - Tells Railway how to run the bot
- `redis_client.py` - Supports REDIS_URL
- `database/engine.py` - Optimized for Railway's connection limits
- `requirements.txt` - All dependencies listed

## Useful Railway CLI Commands

```bash
# Login
railway login

# View project info
railway status

# View logs
railway logs

# Open shell
railway shell

# Set variable
railway variables set TELEGRAM_BOT_TOKEN=your_token

# View all variables
railway variables
```

## Next Steps

1. Monitor the bot in Railway's logs for the first 24 hours
2. Test all bot features thoroughly
3. Set up monitoring/alerts for errors
4. Consider upgrading to paid plan for always-on workers
5. Back up your database regularly

## Support

- Railway Docs: https://docs.railway.app
- Telegram Bot API: https://core.telegram.org/bots/api
- Issues: Check Railway logs or GitHub issues
