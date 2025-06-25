from discord import Interaction
from discord.ext import commands
from database.db import get_all_books, format_books


def register_slash_commands(bot: commands.Bot):
    @bot.tree.command(name="hello", description="Przywitaj się z botem")
    async def hello(interaction: Interaction):
        '''After using a command on discord, the bot says "hello [users name]!"'''
        await interaction.response.send_message(f"Hello {interaction.user.mention}!")
    

    @bot.tree.command(name="show_books", description="Pokaż wszystkie książki w bibliotece")
    async def show_books(interaction: Interaction):
        books = get_all_books()
        message = format_books(books)
        await interaction.response.send_message(message)
    

    @bot.tree.command(name="ping")
    async def ping(interaction: Interaction):
        await interaction.response.send_message("pong!")
