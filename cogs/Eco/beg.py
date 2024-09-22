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



class beg(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def beg(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        money = randrange(1, 101)
        
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            chk = discord.Embed(title=f"**You Are Not Registered!**", color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=chk)
            return

        else:
            ee = discord.Embed(description=f"**{name}** has donated {money} {gem} to {ctx.author.mention}!",color=0x00ff00,timestamp=ctx.message.created_at)
            await ctx.send(embed=ee)
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (money, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", (f"Received By Begging", "+" + f"{money}", time, ctx.author.id))
            db.commit()
            
            return
                    

    @beg.error
    async def beg_error(self,ctx, error):
        
        time = math.ceil(error.retry_after)
        timer = (datetime.timedelta(seconds=time))
        if isinstance(error, commands.CommandOnCooldown):
            embd = discord.Embed(title=f"You can use this command again in **`{timer}`**!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embd)
        else:
            raise error



def setup(bot):
	bot.add_cog(beg(bot))