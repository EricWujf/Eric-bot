import discord
from discord.ext import commands
from core.classes import Cog_extension

class NewCmds(Cog_extension):

    @commands.command()
    async def 建議(self, ctx, message):
        embed=discord.Embed(title="Eric Bot 建議表單", color=0xff0000)
        embed.add_field(name="建議內容", value={message}, inline=False)
        await ctx.send(embed=embed)
        print('Eric Bot >> 建議內容:', {message})

def setup(bot):
    bot.add_cog(NewCmds(bot))