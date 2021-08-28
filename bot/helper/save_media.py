import asyncio
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from .helpers import str_to_b64
from bot import app,sudo_users,db_channel,bot_username,data


async def ForwardToChannel(Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(db_channel)
        return __SENT
    except FloodWait as sl:
        return await ForwardToChannel(app, message, editable)

async def SaveMediaInChannel(Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(db_channel)
        file_er_id = str(forwarded_msg.message_id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            parse_mode="Markdown", disable_web_page_preview=True)
        share_link = f"https://t.me/{bot_username}?start=Encode265_{str_to_b64(file_er_id)}"
        await editable.edit(
            f"**Your File Stored in my Database!**\n\nHere is the Permanent Link of your file: {share_link} \n\n"
            f"Just Click the link to get your file!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton("Open Link", url=share_link)
                ]
                ]
            ),
            disable_web_page_preview=True
        )

    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
