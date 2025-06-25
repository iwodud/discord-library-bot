from discord.ext import commands

from database.db import get_all_books, format_books


def register_commands(bot):
    '''After using a command on discord, the bot says "hello [users name]!"'''
    @bot.command()
    async def hello(ctx):
        await ctx.send(f'Hello {ctx.author.mention}!')
    

    @bot.command()
    async def show_books(ctx):
        books = get_all_books()
        await ctx.send(format_books(books))
