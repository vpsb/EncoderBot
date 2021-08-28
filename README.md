# Encoder Bot 📯
A Telegram Bot To Encode x265 (HEVC) / x264 (AVC) Via FFMPEG

> Added Optimize Settings To Encode x265 :)

### Configuration
Add Values In Environment Variables or Add Them In [config.env](./config.env).

- `API_ID` - Get It By Creating an App On [https://my.telegram.org](https://my.telegram.org)
- `API_HASH` - Get It By Creating an App On [https://my.telegram.org](https://my.telegram.org)
- `BOT_TOKEN` - Get It By Creating an Bot On [https://t.me/BotFather](https://t.me/BotFather)
- `BOT_USERNAME` - Username Of the Bot Without '@'
- `SUDO_USERS` - Chat Identifier Of The Sudo Users.
- `UPDATES_CHANNEL` - (Optional) Updates Channel ID (eg: -105446648712)
- `DB_CHANNEL` - Database Channel ID (eg: -105446648712) Database Channel To Store Files
- `DOWNLOAD_DIR` - (Optional) Temporary Download Directory To Keep Downloaded Files.


### Configuring Encoding Format
To Change The FFMPEG Profile Edit Them In [ffmpeg_utils.py](./ffmpeg_utils.py)

- Already Optimized For Some Qualities :)

### Installing Requirements
Install The Required Python Modules In Your Machine.
```sh
apt-get -qq install ffmpeg
pip3 install -r requirements.txt
```
### Deployment
With Python3.7 or Later.
```sh
python3 main.py
```

### Deploying on Heroku

- Fork The Repository
- Create an App On Heroku Add [The FFMPEG Buildpack](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest) and [Python Build Buildpack](https://heroku.com/Python)
- Fill In [config.env](./config.env)
- Deploy

### Credits
*Thanks to [ShannonScott](https://gist.github.com/ShannonScott) for [transcode_h265.py](https://gist.github.com/ShannonScott/6d807fc59bfa0356eee64fad66f9d9a8)*

### Copyright & License
- Copyright &copy; 2021 &mdash; [Adnan Ahmad](https://github.com/viperadnan-git)
- Licensed Under The Terms Of The [GNU General Public License Version 3 &dash; 29 June 2007](./LICENSE)
