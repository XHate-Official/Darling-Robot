import html
import random
import time

from DarlingRobot import dispatcher
from DarlingRobot.modules.disable import DisableAbleCommandHandler
from DarlingRobot.modules.helper_funcs.chat_status import is_user_admin
from DarlingRobot.modules.helper_funcs.extraction import extract_user
from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext

pfps == ("@BotXpfp", filter=InputMessagesFilterPhotos)

pfps = [
    "./ZeroxDarling/pfp/pfp1.png",
    "./Zeroxdarling /pfp/pfp2.png",
    "./Zeroxdarling /pfp/pfp3.png",
    "./Zeroxdarling /pfp/pfp4.png",
    "./Zeroxdarling /pfp/pfp5.png",
    "./Zeroxdarling /pfp/pfp6.png",
    "./Zeroxdarling /pfp/pfp7.png",
    "./Zeroxdarling /pfp/pfp8.png",
    "./Zeroxdarling /pfp/pfp9.png",
    "./Zeroxdarling /pfp/pfp10.png",
]



def pfp(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pfp_type = random.choice(("pfps"))
    if pfp_type == "Photo":
        try:
            temp = random.choice(pfps)
            reply_to.reply_animation(temp)
        except BadRequest:
            pfp_type = "Photo"

    if pfp_type == "Photo":
        temp = random.choice(pfps)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


PFP_HANDLER = DisableAbleCommandHandler("pfp", pat, run_async=True)

dispatcher.add_handler(PFP_HANDLER)


__handlers__ = [
    PFP_HANDLER,
]
