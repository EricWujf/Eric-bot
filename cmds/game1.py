import discord
from discord.ext import commands
from core.classes import Cog_extension
import random
import json

with open('settings.json', mode='r', encoding='utf8') as setting:
    setting = json.load(setting)


class game1(Cog_extension):

    @commands.command()
    async def faq(self, ctx, message):
        msg = random.choice(setting['game2'])
        embed=discord.Embed(title="Eric Bot隨機問答", color=0xe78b23)
        embed.add_field(name={message}, value=msg, inline=False)
        await ctx.send(embed=embed)

    @commands.group()
    async def dice(self, ctx):
        pass

    @dice.command()
    async def 一(self, ctx):
        dicepoint = random.choice(setting['game1'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="1", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)

    @dice.command()
    async def 二(self, ctx):
        dicepoint = random.choice(setting['game1-2'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="2", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)

    @dice.command()
    async def 三(self, ctx):
        dicepoint = random.choice(setting['game1-3'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="3", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)

    @dice.command()
    async def 四(self, ctx):
        dicepoint = random.choice(setting['game1-4'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="4", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)

    @dice.command()
    async def 五(self, ctx):
        dicepoint = random.choice(setting['game1-5'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="5", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)
    
    @dice.command()
    async def 六(self, ctx):
        dicepoint = random.choice(setting['game1-6'])
        embed=discord.Embed(title="Eric Bot骰子遊戲", color=0xe78b23)
        embed.add_field(name="骰子數量", value="6", inline=False)
        embed.add_field(name="恭喜你骰到了", value=dicepoint, inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(game1(bot))