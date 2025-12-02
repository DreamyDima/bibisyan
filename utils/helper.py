import random
from database.models import Card
from utils.rarity import RARITY_WEIGHTS

def choose_random_card(session):
    cards = session.query(Card).all()
    if not cards:
        return None
    weights = [c.rarity_weight for c in cards]
    return random.choices(cards, weights=weights, k=1)[0]