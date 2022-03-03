import random, re, string, io, asyncio
from io import BytesIO
from typing import Optional, List
from telegram import Message, Update, Bot, User
from pathlib import Path
import glob
import os

from typing import Optional, List
from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

import nltk # shitty lib, but it does work
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


from DarlingRobot import dispatcher
from DarlingRobot.modules.disable import DisableAbleCommandHandler, DisableAbleRegexHandler

# D A N K modules by @deletescape vvv

# based on https://github.com/wrxck/mattata/blob/master/plugins/copypasta.mattata
@run_async
def copypasta(bot: Bot, update: Update):
    message = update.effective_message
    emojis = ["😂", "😂", "👌", "✌", "💞", "👍", "👌", "💯", "🎶", "👀", "😂", "👓", "👏", "👐", "🍕", "💥", "🍴", "💦", "💦", "🍑", "🍆", "😩", "😏", "👉👌", "👀", "👅", "😩", "🚰"]
    reply_text = random.choice(emojis)
    b_char = random.choice(message.reply_to_message.text).lower() # choose a random character in the message to be substituted with 🅱️
    for c in message.reply_to_message.text:
        if c == " ":
            reply_text += random.choice(emojis)
        elif c in emojis:
            reply_text += c
            reply_text += random.choice(emojis)
        elif c.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(random.getrandbits(1)):
                reply_text += c.upper()
            else:
                reply_text += c.lower()
    reply_text += random.choice(emojis)
    message.reply_to_message.reply_text(reply_text)


@run_async
def bmoji(bot: Bot, update: Update):
    message = update.effective_message
    b_char = random.choice(message.reply_to_message.text).lower() # choose a random character in the message to be substituted with 🅱️
    reply_text = message.reply_to_message.text.replace(b_char, "🅱️").replace(b_char.upper(), "🅱️")
    message.reply_to_message.reply_text(reply_text)


@run_async
def clapmoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "👏 "
    reply_text += message.reply_to_message.text.replace(" ", " 👏 ")
    reply_text += " 👏"
    message.reply_to_message.reply_text(reply_text)
    
    
@run_async
def angrymoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "😡 "
    for i in message.reply_to_message.text:
        if i == " ":
            reply_text += " 😡 "
        else:
            reply_text += i
    reply_text += " 😡"
    message.reply_to_message.reply_text(reply_text)
    
    
@run_async
def crymoji(bot: Bot, update: Update):
    message = update.effective_message
    reply_text = "😭 "
    for i in message.reply_to_message.text:
        if i == " ":
            reply_text += " 😭 "
        else:
            reply_text += i
    reply_text += " 😭"
    message.reply_to_message.reply_text(reply_text)
    

@run_async
def me_too(bot: Bot, update: Update):
    message = update.effective_message
    if random.randint(0, 100) > 60:
        reply = random.choice(["Me too thanks", "Haha yes, me too", "Same lol", "Me irl"])
        message.reply_text(reply)
        
        
 @run_async
 def darling(bot: Bot, update: Update):
     message = update.effective_message
     if random.randint(0,100) > 60:
         reply = random.choice(["@X_Hate is My Darling", "@X_Hate Mine", "Yes My darling is @X_Hate" , "@X_Hate is mine"])
         message.reply_text(reply)     
        
        
__help__ = """
- Reply to a text with /🅱️ or /😂 or /👏
- You can also use the text version of these : /bmoji or /copypasta or /clapmoji
"""

__mod_name__ = "Emojis"

COPYPASTA_HANDLER = DisableAbleCommandHandler("copypasta", copypasta)
COPYPASTA_ALIAS_HANDLER = DisableAbleCommandHandler("😂", copypasta)
CLAPMOJI_HANDLER = DisableAbleCommandHandler("clapmoji", clapmoji)
CLAPMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("👏", clapmoji)
ANGRYMOJI_HANDLER = DisableAbleCommandHandler("angrymoji", angrymoji)
ANGRYMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("😡", angrymoji)
CRYMOJI_HANDLER = DisableAbleCommandHandler("crymoji", crymoji)
CRYMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("😭", crymoji)
BMOJI_HANDLER = DisableAbleCommandHandler("🅱️", bmoji)
BMOJI_ALIAS_HANDLER = DisableAbleCommandHandler("bmoji", bmoji)

dispatcher.add_handler(COPYPASTA_HANDLER)
dispatcher.add_handler(COPYPASTA_ALIAS_HANDLER)
dispatcher.add_handler(CLAPMOJI_HANDLER)
dispatcher.add_handler(CLAPMOJI_ALIAS_HANDLER)
dispatcher.add_handler(ANGRYMOJI_HANDLER)
dispatcher.add_handler(ANGRYMOJI_ALIAS_HANDLER)
dispatcher.add_handler(CRYMOJI_HANDLER)
dispatcher.add_handler(CRYMOJI_ALIAS_HANDLER)
dispatcher.add_handler(BMOJI_HANDLER)
dispatcher.add_handler(BMOJI_ALIAS_HANDLER)