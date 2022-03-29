from telethon import custom, events, Button
import os,re
import asyncio

from DarlingRobot import telethn as bot
from DarlingRobot import telethn as tgbot
from DarlingRobot import telethn as aasf
from DarlingRobot.events import register 

edit_time = 5
zero1 = "https://telegra.ph/file/8c85a958e7e60123f0989.jpg"
zero2 = "https://telegra.ph/file/1cf80ad46f2cdb754266e.jpg"
zero3 = "https://telegra.ph/file/eafefc2558b876818d714.jpg"
zero4 = "https://telegra.ph/file/7878a1946e9ea336d7f2c.jpg"

@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("• ᴄʟɪᴄᴋ ʜᴇʀᴇ •",data="information")]]
  on = await aasf.send_message(event.chat, f"**❀ Hᴏɪ.. {(event.sender.first_name)}**\n\n**❀ I Aᴍ [ᴢᴇʀᴏ ᴛᴡᴏ](https://t.me/DarlingXRobot)**\n**❀ Mʏ ᴅᴀʀʟɪɴɢ ɪs [Aᴀʀᴀᴠ](t.me/X_Hate)**\n*❀ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ɪɴғᴏ*", file=zero1, buttons=button)

  await asyncio.sleep(edit_time)
  ok = await aasf.edit_message(event.chat_id, on, file=zero2, buttons=button) 

  await asyncio.sleep(edit_time)
  ok2 = await aasf.edit_message(event.chat_id, ok, file=zero3, buttons=button)

  await asyncio.sleep(edit_time)
  ok3 = await aasf.edit_message(event.chat_id, ok2, file=zero1, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok4 = await aasf.edit_message(event.chat_id, ok3, file=zero3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok5 = await aasf.edit_message(event.chat_id, ok4, file=zero2, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok6 = await aasf.edit_message(event.chat_id, ok5, file=zero3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok7 = await aasf.edit_message(event.chat_id, ok6, file=zero1, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    ZERO = "❀ ʏᴏᴜʀ ᴅᴇᴛᴀɪʟs ʙʏ ᴢᴇʀᴏ ᴛᴡᴏ \n"
    ZERO += f"➻ ғɪʀsᴛ ɴᴀᴍᴇ : {PRO.first_name} \n"
    ZERO += f"➻ ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
    ZERO += f"➻ ʏᴏᴜ ʙᴏᴛ? : {PRO.bot} \n"
    ZERO += f"➻ ʀᴇsᴛʀɪᴄᴛᴇᴅ? : {PRO.restricted} \n"
    ZERO += f"➻ ʏᴏᴜʀ ɪᴅ : {boy}\n"
    ZERO += f"➻ ʏᴏᴜʀ ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
    await event.answer(ZERO, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

__mod_name__ = "✘ ᴍʏ ɪɴғᴏ ✘"

__help__ = """
 ~ /myinfo *:* Get Your Details On Inline. 
"""