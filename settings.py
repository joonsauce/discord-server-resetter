import discord
from discord.ext import commands
from secrets import *

prefix = "dsr!"
description = "Discord Server Resetter v0.0.1b"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Status: OK")
    await bot.change_presence(activity=discord.Game(description))