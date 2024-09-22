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


class leaderboard(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @commands.command(aliases=['xpld', 'xplb'])
    async def xpleaderboard(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        try:
                
            xp = cursor.execute(f"SELECT * FROM experience WHERE guild_id = {ctx.author.guild.id} ORDER BY totalxp DESC LIMIT 10").fetchall()
                
            var = 1
            emd = discord.Embed(title=f"**:scroll: {ctx.author.guild} - XP Leaderboard :scroll:**",color=0xffa500,timestamp=ctx.message.created_at)
            emd.set_thumbnail(url=ctx.author.guild.icon_url)
                
                
            for x in xp:
                emd.add_field(name=f"**`#{var}` {self.bot.get_user(x[0])}**", value=f"**XP - {x[4]}**", inline=False)
                var += 1
                    
            await ctx.send(embed=emd)
                
        except Exception as e:
            print(e)



    @commands.command(aliases=['lb','ld'])
    async def leaderboard(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        try:
                
            lb = cursor.execute("SELECT * FROM economy ORDER BY wallet DESC LIMIT 10").fetchall()
                
            var = 1
            emd = discord.Embed(title=f"**:scroll: Global Eco Leaderboard :scroll:**",color=0xffa500,timestamp=ctx.message.created_at)
            emd.set_thumbnail(url= self.bot.user.avatar_url)
                
                
            for l in lb:
                emd.add_field(name=f"**`#{var}` {self.bot.get_user(l[0])}**", value=f"**Gems - {l[1]} {gem}**", inline=False)
                var += 1
                    
            await ctx.send(embed=emd)
                
        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(leaderboard(bot))