# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Asena UserBot - Yusuf Usta
#

''' It was the module that helps in banning spammers joining the group. '''

from asyncio import sleep
from requests import get

from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, ANTI_SPAMBOT, ANTI_SPAMBOT_SHOUT, bot


@bot.on(ChatAction)
async def anti_spambot(welcm):
    try:
        ''' If a user matches the spam algorithm
           bans him from the group. '''
        if not ANTI_SPAMBOT:
            return
        if welcm.user_joined or welcm.user_added:
            adder = None
            ignore = False
            users = None

            if welcm.user_added:
                ignore = False
                try:
                    adder = welcm.action_message.from_id
                except AttributeError:
                    return

            async for admin in bot.iter_participants(
                    welcm.chat_id, filter=ChannelParticipantsAdmins):
                if admin.id == adder:
                    ignore = True
                    break

            if ignore:
                return

            elif welcm.user_joined:
                users_list = hasattr(welcm.action_message.action, "users")
                if users_list:
                    users = welcm.action_message.action.users
                else:
                    users = [welcm.action_message.from_id]

            await sleep(5)
            spambot = False

            if not users:
                return

            for user_id in users:
                async for message in bot.iter_messages(welcm.chat_id,
                                                       from_user=user_id):

                    correct_type = isinstance(message, Message)
                    if not message or not correct_type:
                        break

                    join_time = welcm.action_message.date
                    message_date = message.date

                    if message_date < join_time:
                        # Eğer mesaj kullanıcı katılma tarihinden daha önce ise yoksayılır.
                        continue

                    check_user = await welcm.client.get_entity(user_id)

                    # Hata ayıklama. İlerideki durumlar için bırakıldı. ###
                    print(
                        f"Participating user: {check_user.first_name} [ID: {check_user.id}]"
                    )
                    print(f"Chat: {welcm.chat.title}")
                    print(f"Time: {join_time}")
                    print(
                        f"Message sent: {message.text}\n\n[Zaman: {message_date}]"
                    )
                    ##############################################

                    try:
                        cas_url = f"https://combot.org/api/cas/check?user_id={check_user.id}"
                        r = get(cas_url, timeout=3)
                        data = r.json()
                    except BaseException:
                        print(
                            "CAS check failed, reverting to old anti_spambot check."
                        )
                        data = None
                        pass

                    if data and data['ok']:
                        reason = f"[Banned by Combot Anti Spam.](https://combot.org/cas/query?u={check_user.id})"
                        spambot = True
                    elif "t.cn/" in message.text:
                        reason = "`t.cn` URL'leri tespit edildi."
                        spambot = True
                    elif "t.me/joinchat" in message.text:
                        reason = "Potansiyel reklam mesajı"
                        spambot = True
                    elif message.fwd_from:
                        reason = "Başkasından iletilen mesaj"
                        spambot = True
                    elif "?start=" in message.text:
                        reason = "Telegram botu `start` linki"
                        spambot = True
                    elif "bit.ly/" in message.text:
                        reason = "`bit.ly` URL'leri tespit edildi."
                        spambot = True
                    else:
                        if check_user.first_name in ("Bitmex", "Promotion",
                                                     "Information", "Dex",
                                                     "Announcements", "Info",
                                                     "Duyuru", "Duyurular"
                                                     "Bilgilendirme", "Bilgilendirmeler"):
                            if check_user.last_name == "Bot":
                                reason = "Bilinen SpamBot"
                                spambot = True

                    if spambot:
                        print(f"Potansiyel Spam Mesajı: {message.text}")
                        await message.delete()
                        break

                    continue  # Bir sonraki mesajı kontrol et

            if spambot:
                chat = await welcm.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if not admin and not creator:
                    if ANTI_SPAMBOT_SHOUT:
                        await welcm.reply(
                            "@admins\n"
                            "`ANTI SPAMBOT TESPİT EDİLDİ!\n"
                            "THIS USER MATCHES MY SPAMBOT ALGORITHMS!`"
                            f"SEBEP: {reason}")
                        kicked = False
                        reported = True
                else:
                    try:

                        await welcm.reply(
                            "`Potential Spambot Detected !!`\n"
                            f"`SEBEP:` {reason}\n"
                            "Kicking from group now, this ID will be saved for future.\n"
                            f"`USER:` [{check_user.first_name}](tg://user?id={check_user.id})"
                        )

                        await welcm.client.kick_participant(
                            welcm.chat_id, check_user.id)
                        kicked = True
                        reported = False

                    except BaseException:
                        if ANTI_SPAMBOT_SHOUT:
                            await welcm.reply(
                                "@admins\n"
                                "`ANTI SPAMBOT DETECTED!\n"
                                "THIS USER MATCHES MY SPAMBOT ALGORITHMS!`"
                                f"SEBEP: {reason}")
                            kicked = False
                            reported = True

                if BOTLOG:
                    if kicked or reported:
                        await welcm.client.send_message(
                            BOTLOG_CHATID, "#ANTI_SPAMBOT RAPORU\n"
                            f"Kullanıcı: [{check_user.first_name}](tg://user?id={check_user.id})\n"
                            f"Kullanıcı IDsi: `{check_user.id}`\n"
                            f"Sohbet: {welcm.chat.title}\n"
                            f"Sohbet IDsi: `{welcm.chat_id}`\n"
                            f"Sebep: {reason}\n"
                            f"Mesaj:\n\n{message.text}")
    except ValueError:
        pass


CMD_HELP.update({
    'anti_spambot':
    "Usage: If this module is enabled in config.env or with env value,\
        \if these spammers match UserBot's anti-spam algorithm,\
        \nThis module bans (or informs admins) spammers from the group."
})
