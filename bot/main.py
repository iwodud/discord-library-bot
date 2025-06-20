import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

import bot_commands


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') #  możliwe, że mode='a'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot_commands.register_commands(bot)


@bot.event
async def on_ready():
    print(f"The {bot.user.name} is ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)


bot.run(token)