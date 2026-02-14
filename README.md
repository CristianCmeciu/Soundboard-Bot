# Discord Soundboard Bot

A dynamic Discord soundboard bot built with `discord.py`.

Any `.mp3` file added to the `sounds/` folder automatically becomes available in the `/play` slash command (with autocomplete).

---

## Setup

### 1. Create a Discord Bot

- Go to the Discord Developer Portal
- Create a new application
- Go to **Bot → Add Bot**
- Copy the bot token

---

### 2. Invite the Bot

Make sure you invite the bot with the following scope:

- `bot`
- `applications.commands`

And give it permission to:
- Connect to Voice Channels
- Speak

---

### 3. Create a `.env` file

Create a file named `.env` in the project root:


---

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Install FFmpeg

FFmpeg is required for voice playback.

Windows

Download from: https://www.gyan.dev/ffmpeg/builds/#release-builds

Extract the archive

Add the bin folder to your System PATH

Linux
sudo apt install ffmpeg

### 6️. Add Sounds

Add any .mp3 files inside the sounds folder.

Each file will automatically be available in the /play command via autocomplete.

No code modification required.

### 7. Run the bot

python bot.py

### Notes

Maximum 25 autocomplete results (Discord limit)
