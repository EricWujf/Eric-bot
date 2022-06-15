import discord
from discord import message
from discord.ext import commands
import json
import os

with open('settings.json', mode='r', encoding='utf8') as setting:
    setting = json.load(setting)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix= 't!')

@bot.event
async def on_ready():
    print('Eric Bot >> 機器人已上線!')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(setting['Token'])