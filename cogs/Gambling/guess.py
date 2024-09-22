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
import json
from botprefix import prefix


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class guess(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def guess(self,ctx, amount : int=None):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
            return
            
        if amount is None:
            emd = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}guess [bet amount]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=emd)
            return
            
        if amount <= 0:
            e = discord.Embed(title=f"Amount Should be Greater than 0!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=e)
            return
            
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if amount > wallet[0]:
            noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Bet!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noe)
            return
            
        if amount < wallet[0]:
            e = discord.Embed(title="Guess a number between 1 and 5, which I'm thinking!",description="**You have 15 seconds! :alarm_clock:**", colour=0xbc8f8f,timestamp=ctx.message.created_at)
            e.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e)
        
        def check(message):
            return message.author == ctx.author
            
        try:
            message = await self.bot.wait_for('message', timeout=15.0, check=check)
            msg = int(message.content)
            ab = [1,2,3,4,5]
            num = int(random.choice(ab))
            
            if msg <= 0 or msg > 5:
                await ctx.send("You have to enter number between 1 and 5!")
                em10 = discord.Embed(title="You have to enter number between 1 and 5!",color=0xff0000,timestamp=ctx.message.created_at)
                em10.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em10)
            
            elif msg == num:
                rem = discord.Embed(title="GG! You got the right number!",description=f"**You Won {math.floor(amount + 85 / 100 * amount)} {gem}!**",color=0x00ff00,timestamp=ctx.message.created_at)
                rem.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
                await ctx.send(embed=rem)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()
                
                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount + 85 / 100 * amount), ctx.author.id))
                db.commit()
                
                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Guess Game", "+" + f"{math.floor(amount + 85 / 100 * amount)}", time, ctx.author.id))
                db.commit()
            
            
            elif msg != num:
                wem = discord.Embed(title=f"Better Luck Next Time! I was thinking **{num}**!",description=f"**You Lost {amount} {gem}!**",color=0xff0000,timestamp=ctx.message.created_at)
                wem.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
                await ctx.send(embed=wem)
                
                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()
                
                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Guess Game", "-" + f"{amount*2}", time, ctx.author.id))
                db.commit()
            
        except asyncio.TimeoutError:
            ee = discord.Embed(title=f"You took too long to answer, **{amount}** {gem} have been deducted from your wallet! **What a dumb!**",colour=0xff0000,timestamp=ctx.message.created_at)
            ee.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=ee)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            return




def setup(bot):
	bot.add_cog(guess(bot))