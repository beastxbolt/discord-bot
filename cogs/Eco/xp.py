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


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class xp(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def xp(self,ctx):
        try:
            xp = cursor.execute(f"SELECT xp FROM experience WHERE user_id = {ctx.author.id} AND guild_id = {ctx.author.guild.id}").fetchone()
            level = cursor.execute(f"SELECT level FROM experience WHERE user_id = {ctx.author.id} AND guild_id = {ctx.author.guild.id}").fetchone()
            totalxp = cursor.execute(f"SELECT totalxp FROM experience WHERE user_id = {ctx.author.id} AND guild_id = {ctx.author.guild.id}").fetchone()
                
            embed = discord.Embed(title=f"XP - **{xp[0]}**\nLevel - **{level[0]}**\nTotal XP - **{totalxp[0]}**", color=0xFF69B4, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            return
        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(xp(bot))