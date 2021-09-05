import os
import requests
from bot import data, download_dir
from pyrogram.types import Message
from .ffmpeg_utils import encode, get_thumbnail, get_duration, get_width_height
from .helpers import str_to_b64
from bot import app, data, sudo_users, bot_username, db_channel
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from .save_media import SaveMediaInChannel

def add_task(message: Message):
    try:
      msg = message.reply_text("<b>Downloading 📯</b>", quote=True)
      filepath = message.download(file_name=download_dir)
      msg.edit(text=f"**Enoding Your File Please Wait 📯**")
      new_file = encode(filepath)
      if new_file:
        msg.edit(text=f"**Video Encoded Successfully 📯**")
        duration = get_duration(new_file)
        thumb = requests.get('https://i.imgur.com/fiNdPwL.jpeg', allow_redirects=True)
        open('img.jpeg', 'wb').write(thumb.content)
        msg.edit(f"**Uploading**")
        file_name = ".".join(new_file.split("/")[-1].split(".")[:-1])
        message.reply_document(new_file,thumb='img.jpeg',caption=f"**✦ {file_name}**")
        os.remove(new_file)
        os.remove('img.jpeg')
        msg.edit(f"**Video Successfully Encoded to x265 📯**")
      else:
        msg.edit(f"**Something Went Wrong While Encoding 📯\nTry Again Later**")
        os.remove(filepath)
    except Exception as e:
      msg.edit(f"```{e}```")
    on_task_complete()
