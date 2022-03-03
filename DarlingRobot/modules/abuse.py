import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "shut up dickhead",
    "asshole ",
    "son of a bitch",
    "U piece of shit",
    "Go and fck urself",
    "Lode randi",
    "and band ka kaath kathola why r u so bahen ka lola",
    "My My! Uk what... u r gey-kun",
    "Bsdk",
    "Dhat teri mkc🙂",
    "Sale Mithai ke dukan pe le jaenge 2 rs me bik jaega",
    "Jhat barabar toh tumhari sakal h aur chale ho laundiya baaji karne",
    "Ek jinda jhat ka baal kya chahta padhai likhai kaam dhandha lekin is bsdwale ki gand me hamesa chull machti h",
    "U think u r special? yea u r but only for my shoes",
    "Vro Dukh dard bhul ja lund pakad ke jhul ja",
    "Aree ree reee ye machli dharti pe kyu h betixhod",
    "Tum bsdwale, tumhare chacha bsdwale, tumhare bete bsdwale, tumhari aane wali awlad bsdwale, tumhara khandan bsdwala, Nikal lode",
    "CHAL CHAL APNI MAAKI CHUCHIYA DIKA",
    "Teri maa RANDI HAI",
    "is lwde ki kya pahchan kholo chaddi maro gand",
    "vsdk yaha se pilega 2km dur jaake pregnent hoga",
    "vro tum toh bade heavy chutiya ho yr",
    "sab chala gaya but aapka chutiyapa nhi gaya",
    "dekh vro teri didi chhat de saiyan saiyan pukar rahi",
    "Nibbe jaa jaake padhai kar",
    "padhle beta padhle warna bada hokar kothe pe jaana padega",
    "jaada gand na phulao yahi patak ke ........ samj ja",
    "la la la la lori tu h bahen ki lodi",
    "kurta pajama kala kala kala kala tu hi h bsdwala wala wala wala wala wala",
    "gori tu bada sarmati h lund pakad ke hamesa jhul jati h",
    "Ab Bol Ab Bolna mdhrxhod",
    "wo dekho chutiya",
    "Randwe bola tha jaada harpik mt pi lekin nhi hume humari gand me toh chull h hum toh piyenge",
    "katrina's najayaj bahen:- Mai itni sundar hu mai kya karu. /nAhem Ahem... Ma xhuda xhuda xhuda xhuda",
    "Ae Bhai thodi aur dalde is lode ki gand faad de",
    "Ye hamara neta h sabka mu me leta",
    "A for apple b for ball kand tum karo tumahara baap kare bawal"
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))




__mod_name__ = "Abuse"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)