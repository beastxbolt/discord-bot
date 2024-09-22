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


class rps(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def rps(self,ctx,type : str = None,*,bet : int = None):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        typelist = ["r", "p", "s"]
        a = random.choice(typelist)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
            return
            
        
        if not type:
            e8m = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}rps [r|p|s] [bet amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=e8m)
            return
            
            
            
        if bet is None:
            await ctx.send("Please specify the bet amount!", delete_after=5)
            return
            
        if bet <= 0:
            await ctx.send("Please specify the bet amount greater than **0**!", delete_after=5)
            return
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if bet > wallet[0]:
            noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Bet!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noe)
            return
            

        
        if type == "r" and a == "r":
            e1 = discord.Embed(title=f"It's A Tie, We Both Chose Rock!",description=":fist: **V/S** :fist:", colour=0x0080ff, timestamp=ctx.message.created_at)
            e1.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e1)
            return
            
            
        elif type == "r" and a == "p":
            e2 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":fist: **V/S** :hand_splayed:", colour=0xff0000, timestamp=ctx.message.created_at)
            e2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e2)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif type == "r" and a == "s":
            e3 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":fist: **V/S** :v:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e3)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (bet*2, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif type == "p" and a == "p":
            e4 = discord.Embed(title=f"It's A Tie, We Both Chose Paper!",description=":hand_splayed: **V/S** :hand_splayed:", colour=0x0080ff, timestamp=ctx.message.created_at)
            e4.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e4)
            return
            
            
        elif type == "p" and a == "r":
            e5 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":hand_splayed: **V/S** :fist:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e5.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e5)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (bet*2, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif type == "p" and a == "s":
            e6 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":hand_splayed: **V/S** :v:", colour=0xff0000, timestamp=ctx.message.created_at)
            e6.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e6)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif type == "s" and a == "s":
            e7 = discord.Embed(title=f"It's A Tie, We Both Chose Scissor!",description=":v: **V/S** :v:", colour=0x0080ff, timestamp=ctx.message.created_at)
            e7.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e7)
            return
            
            
        elif type == "s" and a == "r":
            e8 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":v: **V/S** :fist:", colour=0xff0000, timestamp=ctx.message.created_at)
            e8.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e8)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            return
            
            
        elif type == "s" and a == "p":
            e9 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":v: **V/S** :hand_splayed:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e9.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e9)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (bet*2, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            return
            
            
            
            
        elif a == "r" and type == "p":
            e10 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":fist: **V/S** :hand_splayed:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e10.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e10)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", bet*2, ctx.author.id)
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            return
            
            
        elif a == "r" and type == "s":
            e11 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":fist: **V/S** :v:", colour=0xff0000, timestamp=ctx.message.created_at)
            e11.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e11)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif a == "p" and type == "r":
            e12 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":hand_splayed: **V/S** :fist:", colour=0xff0000, timestamp=ctx.message.created_at)
            e12.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e12)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif a == "p" and type == "s":
            e13 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":hand_splayed: **V/S** :v:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e13.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e13)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (bet*2, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif a == "s" and type == "r":
            e14 = discord.Embed(title=f"You Won {bet*2} {gem}!",description=":v: **V/S** :fist:", colour=0x00ff00, timestamp=ctx.message.created_at)
            e14.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e14)
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (bet*2, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won In Rock, Paper & Scissor", "+" + f"{bet*2}", time, ctx.author.id))
            db.commit()
            
            return
            
            
        elif a == "s" and type == "p":
            e15 = discord.Embed(title=f"You Lost {bet} {gem}!",description=":v: **V/S** :hand_splayed:", colour=0xff0000, timestamp=ctx.message.created_at)
            e15.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e15)
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (bet, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Lost In Rock, Paper & Scissor", "-" + f"{bet}", time, ctx.author.id))
            db.commit()
            
            return
            
        if type != "r":
            e16 = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}rps [r|p|s] [bet amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=e16)
            return
            
        if type != "p":
            e17 = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}rps [r|p|s] [bet amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=e17)
            return
            
        if type != "s":
            e18 = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}rps [r|p|s] [bet amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=e18)
            return



def setup(bot):
	bot.add_cog(rps(bot))