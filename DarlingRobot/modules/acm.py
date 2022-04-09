import requests
import html
from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    Filters,
    run_async,
    MessageHandler,
)
from telegram.utils.helpers import mention_html
from DarlingRobot.modules.sql import acm_sql
from DarlingRobot import DRAGONS, dispatcher, TOKEN
from DarlingRobot.modules.disable import DisableAbleCommandHandler
from DarlingRobot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_restrict,
    user_admin,
    connection_status,
    ADMIN_CACHE,
)

from DarlingRobot.modules.helper_funcs.extraction import (
    cextract_user,
    cextract_user_and_text,
)
from DarlingRobot.modules.log_channel import loggable
from DarlingRobot.modules.helper_funcs.alternate import send_message

from DarlingRobot.modules.sql import acm_sql
from DarlingRobot.modules.helper_funcs.decorators import DARLINGCMD

from ..modules.helper_funcs.anonymous import userr_admin, AdminPerms


# Is Antichannelmode on or off
@bot_admin
@user_admin
def cleanlinked(update: Update, context: CallbackContext):
    args = context.args
    chat = update.effective_chat
    msg = update.effective_message
    if args:
        if len(args) != 1:
            msg.reply_text("Invalid arguments!")
            return
        param = args[0]
        if (
            param == "on"
            or param == "true"
            or param == "yes"
            or param == "On"
            or param == "Yes"
            or param == "True"
        ):
            acm_sql.setCleanLinked(chat.id, True)
            msg.reply_text(
                f"*Enabled* cleanlinked in {chat.title}. Messages sent by channel will be deleted.",
                parse_mode=ParseMode.MARKDOWN,
            )
            return
        elif (
            param == "off"
            or param == "false"
            or param == "no"
            or param == "No"
            or param == "Off"
            or param == "False"
        ):
            acm_sql.setCleanLinked(chat.id, False)
            msg.reply_text(
                f"*Disabled* cleanlinked in {chat.title}.",
                parse_mode=ParseMode.MARKDOWN,
            )
            return
        else:
            msg.reply_text(
                "Your input was not recognised as one of: yes/no/on/off"
            )  # on or off ffs
            return
    else:
        stat = acm_sql.getCleanLinked(str(chat.id))
        if stat:
            msg.reply_text(
                f"Linked channel post deletion is currently *enabled* in {chat.title}. Messages sent from the linked channel will be deleted.",
                parse_mode=ParseMode.MARKDOWN,
            )
            return
        else:
            msg.reply_text(
                f"Linked channel post deletion is currently *disabled* in {chat.title}.",
                parse_mode=ParseMode.MARKDOWN,
            )
            return


# Ban all channel of that user and delete the channel sent message
# Credits To -> https://t.me/ShalmonAnandMate | https://github.com/ShalmonAnandMate
# This Module is made by Shalmon. Do Not Edit this part !!
def sfachat(update: Update, context: CallbackContext):
    msg = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot = context.bot
    hmm = "Here's the link"
    if user and user.id == 136817688:
        cleanlinked = acm_sql.getCleanLinked(str(chat.id))
        if cleanlinked:
            linked_group_channel = bot.get_chat(chat.id)
            lgc_id = linked_group_channel.linked_chat_id
            if str(update.message.sender_chat.id) == str(lgc_id):
                return ""
            BAN_CHAT_CHANNEL = f"https://api.telegram.org/bot{TOKEN}/banChatSenderChat?chat_id={update.message.chat.id}&sender_chat_id={update.message.sender_chat.id}"
            respond = requests.post(BAN_CHAT_CHANNEL)
            if respond.status_code == 200:
                BANNED_CHANNEL_LINK = (
                    f"t.me/c/{update.message.sender_chat.id}/1".replace("-100", "")
                )
                update.message.reply_text(
                    f"""
• AUTO-BAN CHANNEL EVENT ‼️
❌ CHANNEL BANNED : <a href="{BANNED_CHANNEL_LINK}">{hmm}</a>
                """,
                    parse_mode=ParseMode.HTML,
                )
            else:
                update.message.reply_text(
                    f"""
There was an error occured during auto ban and delete message. please report this to @Shinobu_Support.
• Error: `{respond}`
                """
                )
            msg.delete()
            return ""


CLEANLINKED_HANDLER = CommandHandler(
    ["antichannel", "cleanlinked"],
    cleanlinked,
    filters=Filters.chat_type.groups,
    run_async=True,
)
SFA_HANDLER = MessageHandler(Filters.all, sfachat, allow_edit=True, run_async=True)

dispatcher.add_handler(SFA_HANDLER, group=69)
dispatcher.add_handler(CLEANLINKED_HANDLER)

__handlers__ = [CLEANLINKED_HANDLER, SFA_HANDLER]
