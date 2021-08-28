import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
bot_username = os.environ.get("BOT_USERNAME")
db_channel = int(os.environ.get("DB_CHANNEL"))
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
log_channel = os.environ.get("LOG_CHANNEL", None)
updates_channel = os.environ.get("UPDATES_CHANNEL")
FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
