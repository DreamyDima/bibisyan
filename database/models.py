from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime, Boolean, func, UniqueConstraint
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
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
    __tablename__ = "user_cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))
    qty = Column(Integer, default=1)

    __table_args__ = (UniqueConstraint("user_id", "card_id", name="uq_user_card"),)

class Drop(Base):
    __tablename__ = "drops"
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer)
    chat_id = Column(Integer)
    card_id = Column(Integer, ForeignKey("cards.id"))
    claimed_by = Column(Integer, ForeignKey("users.id"))
    posted_at = Column(DateTime(timezone=True), server_default=func.now())

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())