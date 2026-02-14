from discord.ext import commands
import discord
from asyncio import run_coroutine_threadsafe
import os
import dotenv

dotenv.load_dotenv()

token = os.getenv("DISCORD_TOKEN")

SOUNDS_PATH = "sounds"

GUILD_ID = 532314047534727172
guild = discord.Object(id=GUILD_ID)

bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

def get_sound_files():
    return [f.replace(".mp3","") for f in os.listdir(SOUNDS_PATH) if f.endswith(".mp3")]

@bot.event
async def on_ready():
    await bot.tree.sync(guild=guild)
    print("Synced")

async def sound_autocomplete(interaction: discord.Interaction, current: str):
    sounds = get_sound_files()
    return [discord.app_commands.Choice(name=s, value=s) for s in sounds if current.lower() in s.lower()]

@bot.tree.command(name="play",description="Plays a sound",guild=guild)
@discord.app_commands.autocomplete(name=sound_autocomplete)
async def sound(interaction: discord.Interaction, name: str):
    if interaction.user.voice:

        await interaction.response.defer()
        
        channel = interaction.user.voice.channel
        voice_client = await channel.connect()

        audio = discord.FFmpegPCMAudio(source=f'{SOUNDS_PATH}/{name}.mp3',executable='ffmpeg/bin/ffmpeg.exe')

        await  interaction.followup.send("Playing sound")
        
        def after(error):
            future = run_coroutine_threadsafe(voice_client.disconnect(),bot.loop)
            try:
                future.result()
            except:
                pass

        if voice_client:
            voice_client.play(audio,after=after)
    else:
        return await interaction.response.send_message("You need to be in a voice channel",ephemeral=True)

bot.run(token)