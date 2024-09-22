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

class coinflip(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(aliases=['cf'])
    async def coinflip(self,ctx, type : str = None, *,amount : int = None):
        
        gem = self.bot.get_emoji(710105510984286238)
        
        a = ["t", "h","t", "h", "h", "t"]
        coin = random.choice(a)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            chk = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=chk)
            return
            
        if type is None:
            intro = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}coinflip [h|t] [bet amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=intro)
            return
            
            
        if amount is None:
            await ctx.send("Please specify the bet amount!", delete_after=5)
            return
            
        if amount <= 0:
            await ctx.send("Please specify the bet amount greater than **0**!", delete_after=5)
            return
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if amount > wallet[0]:
            nooe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Bet!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=nooe)
            return
            
        if coin == "h" and type == "h":
            file1 = discord.File('./Assets/head.png', filename='head.png')
            h1 = discord.Embed(title=f"You Flipped Heads!",description=f"You Won {math.floor(amount + 85 / 100 * amount)} {gem}!", colour=0x00ff00, timestamp=ctx.message.created_at)
            h1.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            h1.set_image(url='attachment://head.png')
            await ctx.send(file=file1, embed=h1)

            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount + 85 / 100 * amount), ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Coin Flip", "+" + f"{math.floor(amount + 85 / 100 * amount)}", time, ctx.author.id))
            db.commit()
            
            return
            
            
            
            
        elif coin == "t" and type == "t":
            file2 = discord.File('./Assets/tail.png', filename='tail.png')
            h2 = discord.Embed(title=f"You Flipped Tails!",description=f"You Won {math.floor(amount + 85 / 100 * amount)} {gem}!", colour=0x00ff00, timestamp=ctx.message.created_at)
            h2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            h2.set_image(url='attachment://tail.png')
            await ctx.send(file=file2, embed=h2)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount + 85 / 100 * amount), ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Coin Flip", "+" + f"{math.floor(amount + 85 / 100 * amount)}", time, ctx.author.id))
            db.commit()
            
            return
            
            
            
        elif type == "h" and coin == "t":
            file3 = discord.File('./Assets/tail.png', filename='tail.png')
            h3 = discord.Embed(title=f"You Flipped Tails!",description=f"You Lost {amount} {gem}!", colour=0xff0000, timestamp=ctx.message.created_at)
            h3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            h3.set_image(url='attachment://tail.png')
            await ctx.send(file=file3, embed=h3)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Coin Flip", "-" + f"{amount}", time, ctx.author.id))
            db.commit()
            
            return
            
            
            
            
        elif type == "t" and coin == "h":
            file4 = discord.File('./Assets/head.png', filename='head.png')
            h4 = discord.Embed(title=f"You Flipped Heads!",description=f"You Lost {amount} {gem}!", colour=0xff0000, timestamp=ctx.message.created_at)
            h4.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            h4.set_image(url='attachment://head.png')
            await ctx.send(file=file4, embed=h4)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Coin Flip", "-" + f"{amount}", time, ctx.author.id))
            db.commit()
            
            return



def setup(bot):
	bot.add_cog(coinflip(bot))