import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from DarlingRobot.events import register
from DarlingRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/901e4456059ee49d50dbf.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**⊱ ───── ஓ๑♡๑ஓ ───── ⊰**\n"
  TEXT +=  f"**ʜᴏɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴍʏsᴇʟғ ᴢᴇʀᴏ ᴛᴡᴏ.** \n\n"
  TEXT += "♡ **ʙᴀᴋᴀ, ɪ'ᴍ ᴀʟɪᴠᴇ** \n\n"
  TEXT += f"♡ **ᴍʏ ᴅᴀʀʟɪɴɢ : [|×✠×|](https://t.me/X_Hate)** \n\n"
  TEXT += "**×͜× ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇꨄ\n**"
  TEXT += "**⊱ ───── ஓ๑♡๑ஓ ───── ⊰**"
  BUTTON = [[Button.url("✘ ʜᴇʟᴘ ✘", "https://t.me/ZeroXDarlingbot?start=help"), Button.url("✘ sᴜᴘᴘᴏʀᴛ ✘", "https://t.me/ZeroTwoXSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
