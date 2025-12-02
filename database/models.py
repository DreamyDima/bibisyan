"""
Database models for the Telegram bot application.
"""

from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, func, UniqueConstraint
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    """
    User model representing a Telegram user.
    
    Attributes:
        id: Primary key.
        username: Telegram username.
        display_name: Display name of the user.
        avatar_file_id: File ID of the user's avatar.
        points: User's accumulated points.
        coins: User's accumulated coins.
        favorite_card_id: FK to the user's favorite card.
        created_at: Account creation timestamp.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    display_name = Column(String)
    avatar_file_id = Column(String)
    points = Column(Integer, default=0)
    coins = Column(Integer, default=0)
    favorite_card_id = Column(Integer, ForeignKey("cards.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    favorite_card = relationship("Card", foreign_keys=[favorite_card_id])


class Card(Base):
    """
    Card model representing a collectible card.
    
    Attributes:
        id: Primary key.
        name: Card name.
        description: Card description.
        rarity: Rarity level of the card.
        rarity_weight: Weight used for random selection.
        points: Points awarded when card is obtained.
        coins: Coins awarded when card is obtained.
        image_file_id: File ID of the card's image.
        owner_id: FK to the card creator (user).
    """
    __tablename__ = "cards"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    rarity = Column(String)
    rarity_weight = Column(Integer)
    points = Column(Integer, default=0)
    coins = Column(Integer, default=0)
    image_file_id = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))


class UserCard(Base):
    """
    User-Card association model for inventory management.
    
    Attributes:
        id: Primary key.
        user_id: FK to the user.
        card_id: FK to the card.
        qty: Quantity of this card owned by the user.
    """
    __tablename__ = "user_cards"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))
    qty = Column(Integer, default=1)

    __table_args__ = (UniqueConstraint("user_id", "card_id", name="uq_user_card"),)


class Drop(Base):
    """
    Drop model representing a card drop event in a group chat.
    
    Attributes:
        id: Primary key.
        message_id: ID of the Telegram message containing the drop.
        chat_id: ID of the chat where the drop occurred.
        card_id: FK to the dropped card.
        claimed_by: FK to the user who claimed the drop.
        posted_at: Timestamp when the drop was posted.
    """
    __tablename__ = "drops"
    
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    chat_id = Column(Integer)
    card_id = Column(Integer, ForeignKey("cards.id"))
    claimed_by = Column(Integer, ForeignKey("users.id"))
    posted_at = Column(DateTime(timezone=True), server_default=func.now())


class Admin(Base):
    """
    Admin model for administrator access control.
    
    Attributes:
        id: Primary key.
        user_id: Telegram user ID of the admin.
        username: Telegram username of the admin.
        password_hash: Bcrypt hash of the admin password.
        created_at: Admin account creation timestamp.
    """
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())