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


class daily(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
            return
            
        check = cursor.execute(f"SELECT premium FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if check[0] == "enabled":
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (750, ctx.author.id))
            db.commit()
            
            em = discord.Embed(title=f"Here are your daily {gem} {ctx.author}", description=f"**750** {gem} have been placed in your wallet! {tada}",colour=0x0000ff,timestamp=ctx.message.created_at)
            
            await ctx.send(embed=em)
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Daily Reward", "+750", time, ctx.author.id))
            db.commit()
            
            return
            
            
        if check[0] == "disabled":
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (500, ctx.author.id))
            db.commit()
            
            em = discord.Embed(title=f"Here are your daily {gem} {ctx.author}", description=f"**500** {gem} have been placed in your wallet! {tada}",colour=0x0000ff,timestamp=ctx.message.created_at)
            
            await ctx.send(embed=em)
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Daily Reward", "+500", time, ctx.author.id))
            db.commit()
            


    @daily.error
    async def daily_error(self,ctx, error):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        time = math.ceil(error.retry_after)
        timer = datetime.timedelta(seconds=time)
        if isinstance(error, commands.CommandOnCooldown):
            embd = discord.Embed(title=f"You Need To Wait **`{timer}`** To Collect Your Daily {gem} Again!",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embd)
        else:
            raise error



def setup(bot):
	bot.add_cog(daily(bot))