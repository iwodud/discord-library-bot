import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='urf-8', mode='w') #  możliwe, że mode='a'
intenst = discord.Intents.default()
intenst.message_content = True
intenst.members = True
