import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from DarlingRobot.events import register
from DarlingRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/44d61a5c0844af1f03239.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**⊱ ───── ஓ๑✯๑ஓ ───── ⊰**\n"
  TEXT +=  f"**ʏᴏ [{event.sender.first_name}](tg://user?id={event.sender.id}), ᴍʏsᴇʟғ ᴢᴇʀᴏ ᴛᴡᴏ.** \n"
  TEXT += "☮︎ **ᴋɪᴅᴅᴏ, ɪ'ᴍ ᴀʟɪᴠᴇ** \n"
  TEXT += f"☮︎ **ᴍʏ ᴍᴀsᴛᴇʀ : [|×✠×|](https://t.me/xD_Zent)** \n"
  TEXT += "**×͜× ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ\n**"
  TEXT += "**⊱ ───── ஓ๑✯๑ஓ ───── ⊰**"
  BUTTON = [[Button.url("✘ ʜᴇʟᴘ ✘", "https://t.me/Foundingtitanbot?start=help"), Button.url("✘ sᴜᴘᴘᴏʀᴛ ✘", "https://t.me/AckermanXClan")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
