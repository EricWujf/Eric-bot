import discord
from discord.ext import commands
from core.classes import Cog_extension

class saymsg(Cog_extension):

    @commands.command()
    async def say(self, ctx, message):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(saymsg(bot))