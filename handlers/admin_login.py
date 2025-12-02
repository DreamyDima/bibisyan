"""
Admin login and logout handler.
"""

import logging
from typing import Dict
from aiogram import Router, types
from database.engine import SessionLocal
from database.models import Admin
from utils.auth import (
    check_password,
    start_admin_session,
    end_admin_session,
    is_admin_logged_in,
)

logger = logging.getLogger(__name__)

router = Router()
state: Dict[int, str] = {}


@router.message(commands=["adminlogin"])
async def admin_login_cmd(m: types.Message) -> None:
    """
    Start the admin login process.
    
    Args:
        m: The message containing the /adminlogin command.
    """
    try:
        uid = m.from_user.id
        state[uid] = "awaiting_password"
        await m.reply("🔐 Enter admin password:")
        logger.info(f"Admin login initiated for user {uid}")
    except Exception as e:
        logger.error(f"Error in admin_login_cmd: {e}")
        await m.reply("❌ An error occurred. Please try again.")


@router.message()
async def admin_login_flow(m: types.Message) -> None:
    """
    Handle the password input for admin login.
    
    Args:
        m: The message containing the admin password.
    """
    try:
        uid = m.from_user.id
        if uid not in state or state[uid] != "awaiting_password":
            return

        password = m.text
        if not password:
            await m.reply("❌ Password cannot be empty.")
            return

        # Check if user is registered as admin
        with SessionLocal() as s:
            admin = s.query(Admin).filter_by(user_id=uid).first()

            if not admin:
                await m.reply("❌ You are not registered as an admin.")
                del state[uid]
                logger.warning(f"Login attempt by non-admin user {uid}")
                return

            if not check_password(password, admin.password_hash):
                await m.reply("❌ Wrong password.")
                del state[uid]
                logger.warning(f"Failed login attempt for admin {uid}")
                return

        # Start admin session
        start_admin_session(uid)
        await m.reply("✅ Login successful.\nWelcome to admin mode.")
        logger.info(f"Admin {uid} logged in successfully")
        del state[uid]
        
    except Exception as e:
        logger.error(f"Error in admin_login_flow: {e}")
        await m.reply("❌ An error occurred during login.")
        if m.from_user.id in state:
            del state[m.from_user.id]


@router.message(commands=["adminlogout"])
async def admin_logout(m: types.Message) -> None:
    """
    Log out an admin user.
    
    Args:
        m: The message containing the /adminlogout command.
    """
    try:
        uid = m.from_user.id

        if not is_admin_logged_in(uid):
            await m.reply("You are not logged in.")
            return

        end_admin_session(uid)
        await m.reply("🔒 Logged out successfully.")
        logger.info(f"Admin {uid} logged out")
        
    except Exception as e:
        logger.error(f"Error in admin_logout: {e}")
        await m.reply("❌ An error occurred during logout.")