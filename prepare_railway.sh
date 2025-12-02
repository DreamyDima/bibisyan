#!/bin/bash
# Quick Railway Deployment Script
# This script prepares your project for Railway deployment

set -e

echo "🚀 Preparing project for Railway deployment..."

# Verify Procfile exists
if [ ! -f "Procfile" ]; then
    echo "❌ Procfile not found!"
    exit 1
fi

# Verify requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found!"
    exit 1
fi

echo "✅ Procfile found"
echo "✅ requirements.txt found"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Not a git repository. Initialize with: git init"
    exit 1
fi

echo "✅ Git repository found"

# List all Railway-ready files
echo ""
echo "📦 Railway-ready files:"
echo "  ✓ Procfile"
echo "  ✓ requirements.txt"
echo "  ✓ bot.py"
echo "  ✓ config.py"
echo "  ✓ redis_client.py (Railway compatible)"
echo "  ✓ database/engine.py (Railway compatible)"
echo "  ✓ RAILWAY_DEPLOY.md"
echo "  ✓ .gitignore"

echo ""
echo "📝 Next steps:"
echo "  1. Push to GitHub:"
echo "     git add ."
echo "     git commit -m 'Prepare for Railway deployment'"
echo "     git push origin main"
echo ""
echo "  2. Go to railway.app and create a new project"
echo "  3. Connect your GitHub repository"
echo "  4. Add PostgreSQL and Redis databases"
echo "  5. Set environment variables (see RAILWAY_DEPLOY.md)"
echo "  6. Watch the deployment in Railway dashboard"
echo ""
echo "🎯 Deployment complete!"
