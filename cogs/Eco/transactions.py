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


class transactions(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(aliases=['tns'])
    async def transactions(self,ctx):
	
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        try:
            
            if result is None:
                em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=em)
                return
                
            else:
        
                tns = cursor.execute(f"SELECT * FROM transactions WHERE user_id = {ctx.author.id} ORDER BY id DESC LIMIT 10").fetchall()
                
                var = 1
                emd = discord.Embed(title="**Your Recent Transactions!**",color=0xffa500,timestamp=ctx.message.created_at)
                emd.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                
                for t in tns:
                    emd.add_field(name=f"**`#{var}` {t[2]} {gem} At {t[3]}**", value=f"**Reason - {t[1]}!**", inline=False)
                    var += 1
                    
                await ctx.send(embed=emd)
                
        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(transactions(bot))