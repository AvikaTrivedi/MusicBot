# DOMIN8or Music Player — The first open-source PyTgCalls based Pyrogram bot to play music in voice chats
[![deploy](https://telegra.ph/file/4f3dee3a87e98d9b6a901.jpg)](https://heroku.com/deploy?template=https://github.com/AvikaTrivedi/MusicBot)

## Note

Neither this, or PyTgCalls are fully stable.

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:m
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


### Yor Beloved [Satyanand](http://t.me/satyanandatripathi)
### [stringsession](https://t.me/pyrogram_string_genrobot)
