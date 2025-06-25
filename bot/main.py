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
    await bot.tree.sync(guild=guild)
    await bot.tree.sync()
    print(f"The {bot.user.name} is ready")


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
    
#     await bot.process_commands(message)


bot.run(token)

    # try:
    #     guild = discord.Object(id=1380933352131002408)
    # except Exception as e:
    #     print(f'Error syncing cimmandx: {e}')

    # GUILD_ID = discord.Object(id=1380933352131002408)