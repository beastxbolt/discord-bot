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

class unload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, module_name = None):

        try:
            if module_name == None:
                embed = discord.Embed(title="Enter Module Name To Unload!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)

            else:
                self.bot.unload_extension(f"cogs.{module_name}")
                embed2 = discord.Embed(title=f"{module_name} Module Unloaded Successfully!",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
        except:
            embed3 = discord.Embed(title=f"Failed To Unload {module_name} Module!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)



def setup(bot):
	bot.add_cog(unload(bot))