import discord
from discord import message
from discord.ext import commands
from core.classes import Cog_extension

class Main(Cog_extension):

    @commands.command()
    async def ping(self, ctx):
        embed=discord.Embed(title="機器人網路延遲", color=0xff0000)
        embed.add_field(name="目前延遲", value=f'{round(self.bot.latency*1000)} ms', inline=False)
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(Main(bot))