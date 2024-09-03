import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

extensions = ["settings", "villagers", "daily"]

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print("Logged in as", bot.user.name, "\nVersion:", discord.__version__)

for extension in extensions:
    bot.load_extension(extension)

bot.run(TOKEN)