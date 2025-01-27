# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Avater UserBot - Thilina Weerasekara


""" UserBot module that contains filter commands. """

from asyncio import sleep
import re
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("filter")

# ████████████████████████████████ #

SMART_OPEN = '"'
SMART_CLOSE = '"'
START_CHAR = ('\'', '"', SMART_OPEN)

def remove_escapes(text: str):
    counter = 0
    res = ""
    is_escaped = False
    while counter < len(text):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
        counter += 1
    return res

def split_quotes(text: str):
    if any(text.startswith(char) for char in START_CHAR):
        counter = 1  # ignore first char -> is some kind of quote
        while counter < len(text):
            if text[counter] == "\\":
                counter += 1
            elif text[counter] == text[0] or (text[0] == SMART_OPEN and text[counter] == SMART_CLOSE):
                break
            counter += 1
        else:
            return text.split(None, 1)

        # 1 to avoid starting quote, and counter is exclusive so avoids ending
        key = remove_escapes(text[1:counter].strip())
        # index will be in range, or `else` would have been executed and returned
        rest = text[counter + 1:].strip()
        if not key:
            key = text[0] + text[0]
        return list(filter(None, [key, rest]))
    else:
        return text.split(None, 1)


@register(incoming=True, disable_edited=True, disable_errors=True)
async def filter_incoming_handler(handler):
    """ Checks if the incoming message contains a filter trigger """
    try:
        if not (await handler.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit("`Bot Non-SQL modunda çalışıyor!!`")
                return
            name = handler.raw_text
            if handler.chat_id == -1001420605284 or handler.chat_id == -1001363514260:
                return

            filters = get_filters(handler.chat_id)
            if not filters:
                filters = get_filters("GENEL")
                if not filters:
                    return

            for trigger in filters:
                pro = re.fullmatch(trigger.keyword, name, flags=re.IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id))
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass

@register(outgoing=True, pattern="^.genelfilter (.*)")
async def genelfilter(event):
    try:
        from userbot.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await event.edit("`Bot running in Non-SQL mode!!`")
        return
    mesj = split_quotes(event.pattern_match.group(1))

    if len(mesj) != 0:
        keyword = mesj[0]
        try:
            string = mesj[1]
        except IndexError:
            string = ""
    else:
        await event.edit(LANG['GENEL_USAGE'])
        return

    msg = await event.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#GENELFILTER\
            \nGrup ID: {event.chat_id}\
            \nFiltre: {keyword}\
            \ N \ pain mesaj66 / 5000 Translation resultssaved for filter reply, please do not delete this message !"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                LANG['NEED_BOTLOG']
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = " **{}** `{} {}`"
    if add_filter("GENEL", keyword, string, msg_id) is True:
        await event.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['ADDED']))
    else:
        await event.edit(success.format(keyword, LANG['GENEL_FILTER'], LANG['UPDATED']))


@register(outgoing=True, pattern="^.filter (.*)")
async def add_new_filter(new_handler):
    """ .filter command is a chat 
