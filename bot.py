import discord
import asyncio
import os
from discord.ext import commands
import datetime
import json
from botprefix import prefix
from config import botToken

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, strip_after_prefix=True, case_insensitive=True, intents=intents)

bot.music = {}
bot.voice_client_attributes = {}

def loadcogs(folder):
    for cog in os.listdir(f"./cogs/{folder}"):
        if cog.endswith(".py"):
            try:
                cog = f"cogs.{folder}.{cog.replace('.py','')}"
                bot.load_extension(cog)
            except Exception as e:
                print(f"{cog} cannot be loaded")
                raise e


loadcogs("Eco")
print("Eco Loaded!")

loadcogs("Fun")
print("Fun Loaded!")

loadcogs("Gambling")
print("Gambling Loaded")

loadcogs("Info")
print("Info Loaded!")

loadcogs("Mod")
print("Mod Loaded!")

loadcogs("Music")
print("Music Loaded!")

loadcogs("Owner")
print("Owner Loaded!")

loadcogs("Utility")
print("Utility Loaded!")

bot.run(botToken)