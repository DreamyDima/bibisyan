# Railway Deployment - Quick Start Guide

Your Telegram bot is now ready to deploy on Railway! 🚀

## ⚡ Super Quick Deploy (5 Minutes)

### 1. Sign Up (1 min)
- Go to [railway.app](https://railway.app)
- Click "Sign up"
- Use GitHub account (recommended)

### 2. Create Project (1 min)
- Click "New Project"
- Select "Deploy from GitHub repo"
- Authorize Railway
- Select `bibisyan` repository
- Click "Deploy"

### 3. Add Databases (2 min)
- Click "+ Add"
- Add "PostgreSQL"
- Click "+ Add"
- Add "Redis"
- Wait for both to provision

### 4. Set Variables (1 min)
Go to "Variables" tab and add:
```
TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
OWNER_ID=YOUR_ID_HERE
```

### 5. Done! ✅
Railway auto-deploys. Check logs to see bot running.

---

## 📋 Detailed Steps

### Step 1: Prepare GitHub
```bash
# Your changes are already committed, just push:
git push origin main
```

### Step 2: Create Railway Project

1. Visit [railway.app](https://railway.app)
2. Sign up or login
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Authorize Railway to access your GitHub
6. Select the `bibisyan` repository
7. Click **"Deploy"**

Railway will start building and deploying your code.

### Step 3: Add PostgreSQL Database

1. In your Railway project, click **"+ Add"**
2. Select **"Database"**
3. Click **"PostgreSQL"**
4. Wait for provisioning (usually 1-2 minutes)

Railway automatically creates:
- Database instance
- `DATABASE_URL` environment variable

### Step 4: Add Redis Cache

1. Click **"+ Add"** again
2. Select **"Database"**
3. Click **"Redis"**
4. Wait for provisioning

Railway automatically creates:
- Redis instance
- `REDIS_URL` environment variable

### Step 5: Set Required Variables

1. Click **"Variables"** tab in Railway
2. Add these variables:

| Variable | Value |
|----------|-------|
| `TELEGRAM_BOT_TOKEN` | Your token from BotFather |
| `OWNER_ID` | Your Telegram user ID |
| `DROP_COOLDOWN_SECONDS` | 3600 |
| `DROP_CHANCE_PER_MSG` | 0.005 |
| `ADMIN_SESSION_EXPIRATION` | 1800 |
| `PYTHONUNBUFFERED` | 1 |

**How to get these values:**
- **TELEGRAM_BOT_TOKEN**: Get from [@BotFather](https://t.me/botfather) on Telegram
- **OWNER_ID**: Send `/start` to [@userinfobot](https://t.me/userinfobot) on Telegram

### Step 6: Verify Deployment

1. Go to **"Deployments"** tab
2. Click the latest deployment
3. View **"Logs"** - you should see:
   ```
   Starting bot polling...
   INFO     Starting bot
   ```

### Step 7: Initialize Database

1. Click on your deployment in Deployments tab
2. Click **"Shell"** tab
3. Run:
   ```bash
   python init_db.py
   ```

### Step 8: Test Your Bot

1. Open Telegram
2. Send a message to your bot
3. Bot should respond

---

## 🔧 What Changed for Railway

### New Files:
- **Procfile** - Tells Railway how to run your bot
- **RAILWAY_DEPLOY.md** - Detailed deployment guide
- **prepare_railway.sh** - Verification script

### Updated Files:
- **redis_client.py** - Now supports Railway's REDIS_URL
- **database/engine.py** - Optimized for Railway's database limits

---

## 💰 Railway Pricing

- **Free Tier**: $5/month credit
  - Enough for small bots
  - Includes PostgreSQL and Redis
  - Auto-sleeps after 30 mins of inactivity

- **Pro Plan**: Pay-as-you-go
  - Always-on workers
  - More resources
  - Better uptime

---

## 📊 Monitoring Your Bot

### View Logs
1. Go to Deployments
2. Click your deployment
3. View Logs in real-time

### Check Status
1. Go to project dashboard
2. See all services (Bot, PostgreSQL, Redis)
3. Green = Running, Red = Error

### Restart Bot
1. Click deployment
2. Click "Restart" button
3. Bot redeploys from current code

---

## 🆘 Troubleshooting

### Bot not responding
```bash
# Check if bot is connected
# View logs for errors
```

### Database errors
```bash
# In Railway Shell:
python -c "from database.engine import engine; print('✅ DB Connected')"
```

### Redis errors
```bash
# In Railway Shell:
python -c "from redis_client import redis_db; print(redis_db.ping())"
```

### View environment
```bash
# In Railway Shell:
env | grep -E "(DATABASE|REDIS|TELEGRAM)"
```

---

## 🎯 Next Steps

1. ✅ Code is Railway-ready
2. ✅ Procfile is configured
3. ✅ Dependencies are listed
4. 📍 **You are here**: Ready to deploy!

### To Deploy Now:
```bash
# Your code is ready! Just:
git push origin main

# Then go to railway.app and follow steps above
```

---

## 📚 Useful Links

- [Railway Documentation](https://docs.railway.app)
- [Railway Pricing](https://railway.app/pricing)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Railway CLI Reference](https://docs.railway.app/reference/cli-api)

---

## 🎓 How Railway Works

1. **Watches GitHub**: When you push code, Railway deploys
2. **Reads Procfile**: Uses it to know how to run your app
3. **Manages Databases**: PostgreSQL and Redis automatically available
4. **Auto-scaling**: Adjusts resources based on usage
5. **Logging**: Stores logs for debugging

---

## 💡 Tips

- Check Railway logs regularly during first deployment
- Set up GitHub notifications for deployments
- Keep backups of important data
- Monitor bot performance and errors
- Consider upgrading to paid plan for production bots

---

**Ready to deploy? Go to [railway.app](https://railway.app) now!** 🚀
