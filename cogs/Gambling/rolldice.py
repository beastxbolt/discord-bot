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


class rolldice(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def rolldice(self,ctx,num : int = None,num2 : int = None,amount : int = None):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()

        if result is None:
            em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
            return
            
        emd = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}rolldice [number1] [number2] [bet amount]``",colour=0xff0000,timestamp=ctx.message.created_at)
        
        em = discord.Embed(title="Choose 2 Numbers Between 1 and 6!",colour=0xff0000,timestamp=ctx.message.created_at)
        
        if not num:
            await ctx.send(embed=emd)
            return
            
        if not num2:
            await ctx.send(embed=emd)
            return
                
        if num > 6 or num2 > 6:
            await ctx.send(embed=em)
            return
                
        if num < 0 or num2 < 0 :
            await ctx.send(embed=em)
            return 
                
        if num == num2:
            
            e = discord.Embed(title=f"You must Choose 2 Different Numbers!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=e)
            return
            
        if not amount:
            er = discord.Embed(title=f"Give Me An Amount to Bet!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=er)
            return
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if amount > wallet[0]:
            noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Bet!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noe)
            return
            
        if amount < 0:
            e = discord.Embed(title=f"Amount Should be Greater than 0!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=e)
            return
            
            
            
        rd = [1,2,3,4,5,6]
        c_chose = random.choice(rd)
        
        if c_chose == num or c_chose == num2:
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (amount*2, ctx.author.id))
            db.commit()
            
            roe = discord.Embed(title=f":game_die:You Rolled **`{c_chose}`**:game_die:!\nYou Won {amount*2} {gem}!",colour=0x00ff00,timestamp=ctx.message.created_at)
            roe.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=roe)
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Roll Dice", "+" + f"{amount}*2", time, ctx.author.id))
            db.commit()
            
            return
            
        else:
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
            db.commit()
            
            loe = discord.Embed(title=f":game_die:You Rolled **`{c_chose}`**:game_die:!\nYou Lost {amount} {gem}!",colour=0xff0000,timestamp=ctx.message.created_at)
            loe.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=loe)
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Roll Dice", "-" + f"{amount}", time, ctx.author.id))
            db.commit()
            
            return



def setup(bot):
	bot.add_cog(rolldice(bot))