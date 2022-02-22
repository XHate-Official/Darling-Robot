from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from DarlingRobot import pbot
from DarlingRobot.utils.errors import capture_err
from DarlingRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/e6b500753e801b7096b59.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""☙ **Hey I'm Zero Two** ☙ 
      
✧ ▬▬ ▬▬ ✦✦ ▬▬ ▬▬ ✧
**✧ Python Version :** `{y()}`
**✦ Library Version :** `{o}`
**✧ Telethon Version :** `{s}`
**✦ Pyrogram Version :** `{z}`
✧ ▬▬ ▬▬ ✦✦ ▬▬ ▬▬ ✧

**×͜× Please Contact My Darling or My Senpai for Repo.×͜×**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✘ Darling ✘", url="t.me/X_Hate"), 
                    InlineKeyboardButton(
                        "✘ Senpai ✘", url="t.me/UpperMoonX1")
                ]
            ]
        )
    )
