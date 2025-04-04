# A Powerful Music And Management Bot
# Property Of Rocks Indian Largest Chatting Group
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali + Kattai Massom + Abhimanyu Singh


import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ ɪ ᴀᴍ ᴀʟᴇxᴀ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ\n✪ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʀᴜɴ /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ ᴏᴡɴᴇʀ    : [ᴀsᴀᴅ ᴀʟɪ](https://t.me/Dr_Asad_Ali)\n┣★ ᴜᴘᴅᴀᴛᴇs › : [ᴀʟᴇxᴀ ʜᴇʟᴘ](https://t.me/Alexa_BotUpdates)┓\n┣★ ʀᴇᴘᴏ › : [ᴀʟᴇxᴀ ʀᴇᴘᴏ](https://github.com/TheTeamAlexa/MentionBot)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ\nᴅᴍ ᴛᴏ ᴍʏ [ᴏᴡɴᴇʀ](https://t.me/Jankari_Ki_Duniya) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=(
            [
                Button.url(
                    "☀︎︎️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ☀︎︎",
                    "https://t.me/plyatypusbot?startgroup=true",
                ),
            ],
            [
                Button.url("☀︎︎ ɢʀᴏᴜᴘ ☀︎︎︎", "https://t.me/Shayri_Music_Lovers"),
                Button.url("☀︎︎ ᴄʜᴀɴɴᴇʟ ☀︎︎", "https://t.me/threehumanbodies"),
            ],
            [
                Button.url("☀︎︎ ʙʀᴏ ☀︎︎️️", "https://t.me/Kattai_massom"),
                Button.url("☀︎︎ ᴋɪɴɢ ☀︎︎︎", "https://t.me/Jankari_Ki_Duniya"),
            ],
        ),
    )


@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ʜᴀɪɪɪ sᴛᴀʀᴛ ᴀᴋᴜ ᴅᴜʟᴜ ᴅɪ ᴘᴍ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ 🥺")
    helptext = "✪ ᴍᴇɴᴜ ᴏғ ᴘʟᴀᴛʏᴘᴜs ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /tagall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ ᴛᴀɢᴀʟʟ ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴍᴇᴍᴜʟᴀɪ ᴛᴀɢ ᴀᴅᴍɪɴ\n✪ ᴋᴀᴍᴜ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ᴅᴇɴɢᴀɴ ᴛᴇxᴛ ʏᴀɴɢ ɴᴀɴᴛɪ ᴅɪɢᴜɴᴀᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴᴛɪᴏɴ.\n✪ `ᴇxᴀᴍᴘʟᴇ : /ᴍᴇɴᴛɪᴏɴᴀʟʟ ʀɪᴄᴋ x ᴋᴏᴋᴏ ʟᴜᴄᴜ!`\n✪ ᴋᴀᴍᴜ ᴊᴜɢᴀ ʙɪsᴀ ᴍᴇʀᴇᴘʟʏ ᴋᴇ ᴘᴇsᴀɴ ʏᴀɴɢ ɪɴɢɪɴ ᴋᴀᴍᴜ ɢᴜɴᴀᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴᴛɪᴏɴ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ ᴄʜᴀɴɴᴇʟ", "https://t.me/threehumanbodies"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ʜᴀɪ sᴛᴀʀᴛ ᴀᴋᴜ ʟᴇᴡᴀᴛ ʀᴄ ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴘᴀᴋᴀɪ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ 🥺")
    helptext = "✪ ᴏɴᴡᴇʀ ᴍᴇɴᴜ ᴜɴᴛᴜᴋ ᴘʟᴀᴛʏᴘᴜs ᴍᴇɴᴛɪᴏɴ\n\n✪ ғᴏᴜɴᴅᴇʀ [ᴄʜᴀʟᴏɴᴅʀᴀ∰](https://t.me/itschalondra)\n✪ ᴏғғɪᴄɪᴀʟ ᴋʜᴜsᴜs ᴜɴғᴜᴋ ғᴇᴄʜᴋʟ\n✪ ᴏᴡɴᴇʀ [ᴋᴏᴋᴏ ᴋᴏɴᴛᴏʟ](https://t.me/urrhellgod)\n✪ ғᴜᴛᴜʀᴇ ᴀɴᴇsᴛʜᴇᴛɪᴄ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("☀︎︎ ғᴏᴜɴᴅᴇʀ", "https://t.me/itschalondra"),
                Button.url("ᴏᴡɴᴇʀ ☀︎︎", "https://t.me/urrhellgod"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ᴄᴜᴍᴀ ʙɪsᴀ ᴅɪᴘᴀᴋᴀɪ ᴅɪ ɢʀᴜᴘ ᴀᴛᴀᴜ ᴄʜ ᴀᴊᴀ"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ᴍᴇᴍᴜʟᴀɪ ᴍᴇɴᴛɪᴏɴ ᴋᴇ sᴇᴍᴜᴀ ᴏʀᴀɴɢ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ʙᴇʀɪᴋᴀɴ sᴀʏᴀ sᴀᴛᴜ ᴀʀɢᴜᴍᴇɴᴛ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ᴀᴋᴜ ɢᴀʙɪsᴀ ᴍᴇᴍᴜʟᴀɪ ᴛᴀɢᴀʟʟ! (ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴛᴜʟɪs sᴇʙᴇʟᴜᴍ ᴀᴋᴜ ᴍᴀsᴜᴋ ɢʀᴜᴘ ɪɴɪ)"
            )
    else:
        return await event.respond(
            "ᴋᴀsɪʜ ᴘᴇsᴀɴ ᴅᴏɴɢ ʙɪᴀʀ ᴀᴋᴜ ʙɪsᴀ ᴍᴜʟᴀɪ ᴛᴀɢᴀʟʟɴʏᴀ ʏᴇᴜ....!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("ᴍᴀᴀғ ᴋᴀᴍᴜ ʙɪsᴀ ᴘᴀᴋᴀɪ ᴀᴋᴜ ᴋᴀʟᴏ ᴋᴀᴍᴜ ᴀᴅᴍɪɴ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ᴄᴜᴍᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ᴀᴛᴜʀ ᴀᴋᴜ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ᴋᴀsɪʜ ᴀᴋᴜ ᴋᴀᴛᴀ ᴋᴀᴛᴀ ʙᴜᴀᴛ ᴛᴀɢᴀʟʟ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ᴀᴋᴜ ɢᴀʙɪsᴀ ᴍᴇᴍᴜʟᴀɪ ᴛᴀɢᴀʟʟ! (ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴛᴜʟɪs sᴇʙᴇʟᴜᴍ ᴀᴋᴜ ᴍᴀsᴜᴋ ɢʀᴜᴘ ɪɴɪ)"
            )
    else:
        return await event.respond(
            "ᴋᴀsɪʜ ᴘᴇsᴀɴ ᴅᴏɴɢ ʙɪᴀʀ ᴀᴋᴜ ʙɪsᴀ ᴍᴜʟᴀɪ ᴛᴀɢᴀʟʟɴʏᴀ ʏᴇᴜ....!"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("ᴏᴋᴇᴇ ᴀᴋᴜ ᴀᴋᴀɴ ʙᴇʀʜᴇɴᴛɪ...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("ʙᴇʀʜᴇɴᴛɪ...")


print(">> WORKING <<")
client.run_until_disconnected()