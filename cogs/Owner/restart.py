import discord
import asyncio
import os
import datetime
import math
import requests
import random
from random import choice, randrange
from asyncio import sleep
from discord.ext import commands
from asyncio import TimeoutError
import sqlite3
from sqlite3 import connect
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import urllib.request

class restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):

        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)

        embed = discord.Embed(title=f"{loading} BOT Is Restarting...",colour=0x00ff00,timestamp=ctx.message.created_at)
        embed2 = discord.Embed(title="BOT Restarted Successfully!",colour=0x00ff00,timestamp=ctx.message.created_at)

        msg = await ctx.send(embed=embed)
        await asyncio.sleep(3)
        await msg.edit(embed=embed2)

        os.system('pm2 restart bot.py')



def setup(bot):
	bot.add_cog(restart(bot))