import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import time
from telegram import InputMediaPhoto, TelegramError
from telegram import Update
from telegram.ext import CallbackContext, run_async

from DarlingRobot import dispatcher

from DarlingRobot.modules.disable import DisableAbleCommandHandler
from DarlingRobot.modules.helper_funcs.alternate import typing_action

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

run_async


def reverse(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat_id = update.effective_chat.id
    bot, args = context.bot, context.args
    rtmid = msg.message_id
    imagename = str(time.time()) + ".png"

    reply = msg.reply_to_message
    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
        elif reply.document:
            file_id = reply.document.file_id
        else:
            msg.reply_text("Reply to an image or sticker to lookup.")
            return
        image_file = bot.get_file(file_id)
        image_file.download(imagename)
        if args:
            txt = args[0]
            try:
                lim = int(txt)
            except:
                lim = 2
        else:
            lim = 2
    elif args and not reply:
        splatargs = msg.text.split(" ")
        if len(splatargs) == 3:
            img_link = splatargs[1]
            try:
                lim = int(splatargs[2])
            except:
                lim = 2
        elif len(splatargs) == 2:
            img_link = splatargs[1]
            lim = 2
        else:
            msg.reply_text("/reverse <link> <amount of images to return.>")
            return
        try:
            urllib.request.urlretrieve(img_link, imagename)
        except HTTPError as HE:
            if HE.reason == "Not Found":
                msg.reply_text("Image not found.")
                return
            elif HE.reason == "Forbidden":
                msg.reply_text(
                    "Couldn't access the provided link, The website might have blocked accessing to the website by bot or the website does not existed."
                )
                return
        except URLError as UE:
            msg.reply_text(f"{UE.reason}")
            return
        except ValueError as VE:
            msg.reply_text(f"{VE}\nPlease try again using http or https protocol.")
            return
    else:
        msg.reply_markdown(
            "Please reply to a sticker, or an image to search it!\nDo you know that you can search an image with a link too? /grs [picturelink] <amount>."
        )
        return

    try:
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": (imagename, open(imagename, "rb")),
            "image_content": "",
        }
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        location = response.headers.get("Location")

        if response != 400:
            xx = bot.send_message(
                chat_id,
                "Please wait this process may take time." "\nPlease wait.",
                reply_to_message_id=rtmid,
            )
        else:
            xx = bot.send_message(
                chat_id,
                "Sorry I was not able to find this please reply the image with /grs again so that I cam try again.",
                reply_to_message_id=rtmid,
            )
            return

        os.remove(imagename)
        match = ParseSauce(location + "&hl=en")
        guess = match["best_guess"]
        if match["override"] and not match["override"] == "":
            imgspage = match["override"]
        else:
            imgspage = match["similar_images"]

        if guess and imgspage:
            xx.edit_text(
                f"[{guess}]({location})\nPlease wait this process may take time....",
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
        else:
            xx.edit_text("Can't Find this piece of shit.")
            return

        images = scam(imgspage, lim)
        if len(images) == 0:
            xx.edit_text(
                f"[{guess}]({location})\n[Visually similar images]({imgspage})"
                "\nCouldn't fetch any images.",
                parse_mode="Markdown",
                disable_web_page_preview=True,
            )
            return

        imglinks = []
        for link in images:
            lmao = InputMediaPhoto(media=str(link))
            imglinks.append(lmao)

        bot.send_media_group(chat_id=chat_id, media=imglinks, reply_to_message_id=rtmid)
        xx.edit_text(
            f"[{guess}]({location})\n[Not Sure But Similar image]({imgspage})",
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    except TelegramError as e:
        print(e)
    except Exception as exception:
        print(exception)


def ParseSauce(googleurl):
    """Parse/Scrape the HTML code for the info we want."""

    source = opener.open(googleurl).read()
    soup = BeautifulSoup(source, "html.parser")

    results = {"similar_images": "", "override": "", "best_guess": ""}

    try:
        for bess in soup.findAll("a", {"class": "PBorbe"}):
            url = "https://www.google.com" + bess.get("href")
            results["override"] = url
    except:
        pass

    for similar_image in soup.findAll("input", {"class": "gLFyf"}):
        url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(
            similar_image.get("value")
        )
        results["similar_images"] = url

    for best_guess in soup.findAll("div", attrs={"class": "r5a77d"}):
        results["best_guess"] = best_guess.get_text()

    return results


def scam(imgspage, lim):
    """Parse/Scrape the HTML code for the info we want."""

    single = opener.open(imgspage).read()
    decoded = single.decode("utf-8")
    if int(lim) > 10:
        lim = 10

    imglinks = []
    counter = 0

    pattern = r"^,\[\"(.*[.png|.jpg|.jpeg])\",[0-9]+,[0-9]+\]$"
    oboi = re.findall(pattern, decoded, re.I | re.M)

    for imglink in oboi:
        counter += 1
        imglinks.append(imglink)
        if counter >= int(lim):
            break

    return imglinks


__help__ = """
   /reverse :- reply to a sticker, or an image to search it!
Do you know that you can search an image with a link too? /reverse picturelink <amount>.
"""
__mod_name__ = "Reverse"

REVERSE_HANDLER = DisableAbleCommandHandler(
    ["pp", "grs", "p"], reverse, pass_args=True, admin_ok=True
)

dispatcher.add_handler(REVERSE_HANDLER)
