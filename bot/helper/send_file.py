import asyncio
from bot import data,sudo_users,db_channel,bot_username,app,FORWARD_AS_COPY
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from .helpers import str_to_b64


async def ReplyForward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"**Here is Sharable Link of this file:**\n"
            f"https://t.me/{bot_username}?start=Encode265_{str_to_b64(str(file_id))}\n\n"
            f"__To Retrive the Stored File, just open the link!__",
            disable_web_page_preview=True, quote=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await ReplyForward(message, file_id)


async def MediaForward(Client, user_id: int, file_id: int):
    try:
        if FORWARD_AS_COPY is True:
            return await app.copy_message(chat_id=user_id, from_chat_id=db_channel,
                                          message_id=file_id)
        elif FORWARD_AS_COPY is False:
            return await app.forward_messages(chat_id=user_id, from_chat_id=db_channel,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return MediaForward(app, user_id, file_id)


async def SendMediaAndReply(Client, user_id: int, file_id: int):
    sent_message = await MediaForward(app, user_id, file_id)
    await ReplyForward(message=sent_message, file_id=file_id)
    await asyncio.sleep(2)
