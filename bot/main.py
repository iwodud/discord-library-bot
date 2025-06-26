import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from bot import bot_commands


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') #  możliwe, że mode='a'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot_commands.register_slash_commands(bot)


@bot.event
async def on_ready():
    GUILD_ID = 1380933352131002408
    guild = discord.Object(id=GUILD_ID)

    synced = await bot.tree.sync(guild=guild)
    print(f"The {bot.user.name} is ready — synced {len(synced)} commands to guild")

bot.run(token)
