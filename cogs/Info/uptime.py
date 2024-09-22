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

start_time = datetime.datetime.utcnow()

class uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def uptime(self, ctx):
        
        now = datetime.datetime.utcnow()
        delta = now - start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        
        if days:
            time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds"
            uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

            embed = discord.Embed(title=f"Uptime - {uptime_stamp}",colour=0xCCCC00,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return
        
        if hours:
            time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds"
            uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

            embed2 = discord.Embed(title=f"Uptime - {uptime_stamp}",colour=0xCCCC00,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return

        if minutes:
            time_format = "**{m}** minutes, and **{s}** seconds"
            uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

            embed3 = discord.Embed(title=f"Uptime - {uptime_stamp}",colour=0xCCCC00,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)
            return

        if seconds:
            time_format = "**{s}** seconds"
            uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)

            embed4 = discord.Embed(title=f"Uptime - {uptime_stamp}",colour=0xCCCC00,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed4)
            return


#-----------------------------------------------------------

def setup(bot):
	bot.add_cog(uptime(bot))