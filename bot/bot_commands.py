from discord.ext import commands


def register_commands(bot):
    @bot.command()
    async def hello(ctx):
        await ctx.send(f'Hello {ctx.author.mention}!')
    