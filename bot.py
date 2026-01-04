import discord
from discord.ext import commands
import os
from config import TOKEN, PREFIX

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# Automatically load all cogs
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

@bot.event
async def on_ready():
    print(f"dread online as {bot.user}")

bot.run(TOKEN)

