from aiogram import types, Router
from config import OWNER_ID

router = Router()

proposal_state = {}

@router.message(commands=["proposecard"])
async def proposecard_cmd(m: types.Message):
    proposal_state[m.from_user.id] = {"step": "name"}
    await m.reply("Send card name:")

@router.message()
async def propose_fsm(m: types.Message):
    uid = m.from_user.id
    if uid not in proposal_state:
        return

    st = proposal_state[uid]

    if st["step"] == "name":
        st["name"] = m.text
        st["step"] = "description"
        await m.reply("Send description:")
        return

    if st["step"] == "description":
        st["description"] = m.text
        st["step"] = "rarity"
        await m.reply("Send rarity:")
        return

    if st["step"] == "rarity":
        st["rarity"] = m.text
        st["step"] = "image"
        await m.reply("Send image:")
        return

    if st["step"] == "image":
        if not m.photo:
            await m.reply("Please send an image.")
            return
        file_id = m.photo[-1].file_id

        await m.bot.send_message(
            OWNER_ID,
            f"📨 New card proposal:\n\n"
            f"Name: {st['name']}\n"
            f"Description: {st['description']}\n"
            f"Rarity: {st['rarity']}"
        )
        await m.bot.send_photo(OWNER_ID, file_id)

        del proposal_state[uid]
        await m.reply("Your proposal has been sent to the admin!")