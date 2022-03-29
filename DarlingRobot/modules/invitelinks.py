import re
import html

from telegram import ParseMode
from telegram.update import Update
from telegram.ext import ChatJoinRequestHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram.utils.helpers import mention_html

from DarlingRobot import dispatcher
from DarlingRobot.modules.helper_funcs.decorators import darlingcallback
from DarlingRobot.modules.helper_funcs.chat_status import user_can_restrict_no_reply, bot_admin
from DarlingRobot.modules.log_channel import loggable


def chat_join_req(upd: Update, ctx: CallbackContext):
    bot = ctx.bot
    user = upd.chat_join_request.from_user
    chat = upd.chat_join_request.chat
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✘ ᴀᴘᴘʀᴏᴠᴇ ✘", callback_data="cb_approve={}".format(user.id)
                ),
                InlineKeyboardButton(
                    "✘ ᴅᴇᴄʟɪɴᴇ ✘", callback_data="cb_decline={}".format(user.id)
                ),
            ]
        ]
    )
    bot.send_message(
        chat.id,
        "This Simp {} wants to join {}".format(
            mention_html(user.id, user.first_name), chat.title or "this chat"
        ),
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML,
    )


@darlingcallback(pattern=r"cb_approve=")
@user_can_restrict_no_reply
@bot_admin
@loggable
def approve_joinreq(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    user = update.effective_user
    chat = update.effective_chat
    match = re.match(r"cb_approve=(.+)", query.data)

    user_id = match.group(1)
    try:
        bot.approve_chat_join_request(chat.id, user_id)
        update.effective_message.edit_text(
            f"Join Request Approved by{mention_html(user.id, user.first_name)}.",
            parse_mode="HTML",
        )
        logmsg = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#JOIN_REQUEST\n"
                f"Approved\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
                f"<b>User:</b> {mention_html(user_id, html.escape(user.first_name))}\n"
        )
        return logmsg
    except Exception as e:
        update.effective_message.edit_text(str(e))
        pass


@darlingcallback(pattern=r"cb_decline=")
@user_can_restrict_no_reply
@bot_admin
@loggable
def decline_joinreq(update: Update, context: CallbackContext) -> str:
    bot = context.bot
    query = update.callback_query
    user = update.effective_user
    chat = update.effective_chat
    match = re.match(r"cb_decline=(.+)", query.data)

    user_id = match.group(1)
    try:
        bot.decline_chat_join_request(chat.id, user_id)
        update.effective_message.edit_text(
            f"Join Request declined by {mention_html(user.id, user.first_name)}.",
            parse_mode="HTML",
        )
        logmsg = (
                f"<b>{html.escape(chat.title)}:</b>\n"
                f"#JOIN_REQUEST\n"
                f"Declined\n"
                f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
                f"<b>User:</b> {mention_html(user_id, html.escape(user.first_name))}\n"
        )
        return logmsg
    except Exception as e:
        update.effective_message.edit_text(str(e))
        pass


dispatcher.add_handler(ChatJoinRequestHandler(callback=chat_join_req, run_async=True))