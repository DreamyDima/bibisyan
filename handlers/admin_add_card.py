from aiogram import types, Router, F
from database.engine import SessionLocal
from database.models import Card
from config import OWNER_ID

router = Router()

user_state = {}  # simple FSM replacement for Acode setup

@router.message(commands=["addcard"])
async def addcard_cmd(m: types.Message):
    if m.from_user.id != OWNER_ID:
        await m.reply("You are not authorized.")
        return
    user_state[m.from_user.id] = {"step": "name"}
    await m.reply("Send card name:")

@router.message()
async def addcard_fsm(m: types.Message):
    uid = m.from_user.id
    if uid not in user_state:
        return

    state = user_state[uid]

    # 1) Card name
    if state["step"] == "name":
        state["name"] = m.text
        state["step"] = "description"
        await m.reply("Now send card description:")
        return

    # 2) Description
    if state["step"] == "description":
        state["description"] = m.text
        state["step"] = "rarity"
        await m.reply("Send rarity (common/uncommon/rare/epic/legendary):")
        return

    # 3) Rarity
    if state["step"] == "rarity":
        state["rarity"] = m.text.lower()
        state["step"] = "points"
        await m.reply("Points value:")
        return

    # 4) Points
    if state["step"] == "points":
        state["points"] = int(m.text)
        state["step"] = "coins"
        await m.reply("Coins value:")
        return

    # 5) Coins
    if state["step"] == "coins":
        state["coins"] = int(m.text)
        state["step"] = "image"
        await m.reply("Send the card image:")
        return

    # 6) Image
    if state["step"] == "image":
        if not m.photo:
            await m.reply("Send an actual picture.")
            return

        file_id = m.photo[-1].file_id

        with SessionLocal.begin() as s:
            card = Card(
                name=state["name"],
                description=state["description"],
                rarity=state["rarity"],
                rarity_weight={"common":70,"uncommon":20,"rare":7,"epic":2,"legendary":1}[state["rarity"]],
                points=state["points"],
                coins=state["coins"],
                image_file_id=file_id,
                owner_id=uid
            )
            s.add(card)

        del user_state[uid]
        await m.reply("Card added successfully! 🎉")