# 
# 
#
# 
# 
# 
""" 
#
#
#
#
ههههههههههههههههههههههههههههههههههههههههههههههههههههههه
"""

import asyncio
import base64
import contextlib

from telethon.errors.rpcerrorlist import ForbiddenError
from telethon.tl import functions, types
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name

from . import zedub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type, unsavegif
from ..helpers.utils import _zedutils
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

plugin_category = "الخدمات"
UNSPAM = gvarstatus("Z_UNSPAM") or "ايقاف البلاغ"


# code by t.me/Ve_G4
async def spam_abusezed(event, sandy, zed, sleeptimem, sleeptimet, DelaySpam=False):
    # sourcery no-metrics
    counter = int(zed[0])
    if len(zed) == 2:
        spam_message = str(zed[1])
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message('@AbuseNotifications', spam_message) # code by t.me/A7_M3
            await asyncio.sleep(4)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            if gvarstatus("spamwork") is None:
                return
            await event.client.send_message('@AbuseNotifications', spam_message) # code by t.me/A7_M3
            await asyncio.sleep(4)
    else:
        return
    if DelaySpam is not True: # code by t.me/Ve_G4
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "**- البلاغـات 📌**\n"
                + f"**- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات**\n"
                + f"**- كليشـة البلاغـات :**\n `{spam_message}`",
            )
            await event.client.send_message(event.chat_id, f"**- بلاغـات_ داخليـه 🚸\n- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات\n- كليشـة البلاغـات :**\n `{spam_message}`")

    elif BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "**- البلاغـات 📌**\n"
            + f"**- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات**\n**- وقت التكـرار :** {sleeptimet} **ثانيـه**\n"
            + f"**- كليشـة البلاغـات :**\n `{spam_message}`",
        )
        await event.client.send_message(event.chat_id, f"**- بلاغـات_ داخليـه 🚸\n- تم تنفيـذ تڪـرار البـلاغـات بنجاح ☑️\n- لـ الدعـم**  [Abuse Notifications ⚠️](tg://user?id=4245000) .\n**- عـدد البلاغـات :** {counter} **مـرات\n- كليشـة البلاغـات :**\n `{spam_message}`")


# code by t.me/Ve_G4
@zedub.zed_cmd(pattern="بلاغ ([\s\S]*)")
async def spammer(event):
    sandy = await event.get_reply_message()
    zed = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    try:
        counter = int(zed[0])
    except Exception:
        return await edit_delete(
            event, "**- ارسـل الامـر بالشكـل التالي**\n\n`.بلاغ` **+ عدد التكرار + الرسالة او بالـرد ع رسالة**\n**- مثـال : .بلاغ 12 بالـرد ع كليشـة البـلاغ**"
        )
    if counter > 50:
        sleeptimet = 4
        sleeptimem = 1
    else:
        sleeptimet = 4
        sleeptimem = 0.3
    await edit_delete(event, f"**⎉╎جـارِ الابـلاغ الداخلـي . . . ⚠️ \n⎉╎لـ الدعم @AbuseNotifications\n⎉╎عـدد البلاغـات ** {zed}", 5)
    addgvar("spamwork", True)
    await spam_abusezed(event, sandy, zed, sleeptimem, sleeptimet)


# code by t.me/Ve_G4
@zedub.zed_cmd(pattern=f"{UNSPAM} ?(.*)",)
async def spammer(event):
    if gvarstatus("spamwork") is not None and gvarstatus("spamwork") == "true":
        delgvar("spamwork")
        return await edit_delete(event, "**- تم ايقـاف البلاغـات .. بنجـاح ✅**")
    return await edit_delete(event, "**- لايوجـد هنـاك بلاغـات لـ إيقافهـا ؟!**")



