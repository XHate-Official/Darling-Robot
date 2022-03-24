import html

import random

import time

from telegram import ParseMode, Update, ChatPermissions

from telegram.ext import CallbackContext, run_async

from telegram.error import BadRequest

import Flare_Robot.modules.animequotes_strings as animequotes_strings

from DarlingRobot import dispatcher

from DarlingRobot.modules.disable import DisableAbleCommandHandler

from DarlingRobot.modules.helper_funcs.chat_status import (is_user_admin)

from DarlingRobot.modules.helper_funcs.extraction import extract_user

@run_async

def animepfp(update: Update, context: CallbackContext):

    message = update.effective_message

    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name

    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo

    reply_photo(

        random.choice(pfp_strings.PFP_IMG))

__help__ = """

 • `/animepfp`*:* gives random anime quotes

 

"""

ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)

__mod_name__ = "Anime pfp's"

__command_list__ = [

    "animepfp"

]

__handlers__ = [

    ANIMEPFP_HANDLER

]