from pyrogram import filters
from bot import app, data, sudo_users,bot_username,db_channel,log_channel
from bot.helper.utils import add_task
from pyrogram import types
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from translation import Translation
from bot.helper.save_media import SaveMediaInChannel
from bot.helper.send_file import SendMediaAndReply
from bot.helper.helpers import b64_to_str, str_to_b64
from translation import Translation

video_mimetype = [
  "video/x-flv",
  "video/mp4",
  "application/x-mpegURL",
  "video/MP2T",
  "video/3gpp",
  "video/quicktime",
  "video/x-msvideo",
  "video/x-ms-wmv",
  "video/x-matroska",
  "video/webm",
  "video/x-m4v",
  "video/quicktime",
  "video/mpeg"
  ]

@app.on_message(filters.command("start") & filters.private)
async def start(Client, cmd: Message):

    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/start":
        await cmd.reply_text(
            text=Translation.HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Updates 🔊", url="https://t.me/AsmSafone"),
                    ],
                    [
                        InlineKeyboardButton("About 📖", callback_data="aboutbot"),
                        InlineKeyboardButton("Developer 👨‍💻", callback_data="aboutdevs")
                    ]
                ]
            )
        )
    else:
        try:
            try:
                file_id = int(b64_to_str(usr_cmd).split("_")[-1])
            except (Error, UnicodeDecodeError):
                file_id = int(usr_cmd.split("_")[-1])
            GetMessage = await app.get_messages(chat_id=db_channel, message_ids=file_id)
            message_ids = []
            if GetMessage.text:
                message_ids = GetMessage.text.split(" ")
            else:
                message_ids.append(int(GetMessage.message_id))
            for i in range(len(message_ids)):
                await SendMediaAndReply(app, user_id=cmd.from_user.id, file_id=int(message_ids[i]))
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")

@app.on_message(filters.user(sudo_users) & filters.incoming & (filters.video | filters.document))
def encode_video(app, message):
    if message.document:
      if not message.document.mime_type in video_mimetype:
        message.reply_text(f"**Invalid Video Format !\nMake Sure Its a Supported Video File**", quote=True)
        return
    message.reply_text(f"**Added To Queue**", quote=True) 
    data.append(message)
    if len(data) == 1:
      add_task(message)

@app.on_callback_query()
async def button(Client, cmd: CallbackQuery):

    cb_data = cmd.data
    if "aboutbot" in cb_data:
        await cmd.message.edit(
            text=Translation.ABOUT_BOT_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Support Group ",
                                             url="https://t.me/AsmSupport")
                    ],
                    [
                        InlineKeyboardButton("Developer 👨‍💻", callback_data="aboutdevs")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="gotohome"),
                        InlineKeyboardButton("Close", callback_data="closeMessage"),
                    ]
                ]
            )
        )

    elif "aboutdevs" in cb_data:
        await cmd.message.edit(
            text=Translation.ABOUT_DEV_TEXT,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Support Group",
                                             url="https://t.me/AsmSupport")
                    ],
                    [
                        InlineKeyboardButton("About 📖", callback_data="aboutbot")
                    ],
                    [
                        InlineKeyboardButton("Back", callback_data="gotohome"),
                        InlineKeyboardButton("Close", callback_data="closeMessage"),
                    ]
                ]
            )
        )

    elif "gotohome" in cb_data:
        await cmd.message.edit(
            text=Translation.HOME_TEXT.format(cmd.message.chat.first_name, cmd.message.chat.id),
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("About 📖", callback_data="aboutbot"),
                        InlineKeyboardButton("Developer 👨‍💻", callback_data="aboutdevs")
                    ]
                ]
            )
        )

    elif "addToBatchFalse" in cb_data:
        await SaveMediaInChannel(app, editable=cmd.message, message=cmd.message.reply_to_message)

    elif "closeMessage" in cb_data:
        await cmd.message.delete(True)

    try:
        await cmd.answer()
    except QueryIdInvalid:
        pass

app.run()
