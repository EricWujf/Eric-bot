import discord
from discord.ext import commands
from core.classes import Cog_extension

class Server(Cog_extension):

    @commands.group()
    async def mcserver(self, ctx):
        pass

    @mcserver.command()
    async def FC(self, ctx):
        embed=discord.Embed(title="FC夢幻峽谷IP", color=0xe78b23)
        embed.add_field(name="伺服器IP", value="ftcy.ddns.net", inline=False)
        embed.add_field(name="伺服器贊助IP", value="不給", inline=False)
        embed.add_field(name="伺服器版本", value="1.12.2 ~ 1.16.5", inline=False)
        await ctx.send(embed=embed)

    @mcserver.command()
    async def 文靜(self, ctx):
        embed=discord.Embed(title="文靜之潭IP", color=0xe78b23)
        embed.add_field(name="伺服器IP", value="Play.qpond.net", inline=False)
        embed.add_field(name="伺服器版本", value="1.11.2", inline=False)
        embed.add_field(name="伺服器材質包連結", value="https://drive.google.com/file/d/1pec8R-wfNnLixzzmEipTeMz-xOM4xDYK/view?usp=sharing", inline=False)
        await ctx.send(embed=embed)

    @mcserver.command()
    async def 仙靈(self, ctx):
        embed=discord.Embed(title="仙靈之都IP", color=0xe78b23)
        embed.add_field(name="伺服器IP", value="mc.fairy-capital.online", inline=False)
        embed.add_field(name="伺服器版本", value="1.16.5", inline=False)
        await ctx.send(embed=embed)

    @mcserver.command()
    async def 霓虹(self, ctx):
        embed=discord.Embed(title="霓虹傳說IP", color=0xe78b23)
        embed.add_field(name="伺服器IP", value="hkrnmc.mchk.tk", inline=False)
        embed.add_field(name="伺服器版本", value="1.18.2", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Server(bot))