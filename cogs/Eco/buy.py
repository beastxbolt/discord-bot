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


class buy(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.group()
    async def buy(self,ctx):
            
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}buy [item_name]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)



    @buy.command()
    async def lootbox(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        money = randrange(200, 2001)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            embed = discord.Embed(title=f"**You Are Not Registered!**", color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if wallet[0] < 1000:
            embed2 = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Buy Loot Box!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return
            
        if wallet[0] >= 1000:
            
            embed3 = discord.Embed(title=f"{tada} Transaction Was Successful! {tada}", colour=0x00ff00, timestamp=ctx.message.created_at)
            embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            embed3.add_field(name="**Item Bought**",value="** :ballot_box: Loot Box :ballot_box:**")
            embed3.add_field(name="**Cost**",value=f"**1000** {gem}")
            await ctx.send(embed=embed3)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (1000, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Bought Item Loot Box", "-1000", time, ctx.author.id))
            db.commit()
            
            await asyncio.sleep(2)
            
            
            ee = discord.Embed(title=f"{tada} Congratulations! You managed to get {money} {gem} from the Loot Box! :ballot_box:", colour=0x00ff00, timestamp=ctx.message.created_at)
            ee.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=ee)
            
            
            cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (money, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", (f"Received From Loot Box", "+" + f"{money}", time, ctx.author.id))
            db.commit()
            return




    @buy.command()
    async def premium(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            chk = discord.Embed(title=f"**You Are Not Registered!**", color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=chk)
            return
            
        pre = cursor.execute(f"SELECT premium FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if pre[0] == "enabled":
            pro = discord.Embed(title=f"You Are Already Having Premium Membership!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=pro)
            return
            
        wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if wallet[0] < 20000:
            noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Buy Premium Membership!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noe)
            return
            
            
        if pre[0] == "disabled":
            pro = discord.Embed(title=f"{tada} Transaction Was Successful! {tada}",color=0x00ff00, timestamp=ctx.message.created_at)
            
            pro.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            pro.add_field(name="**Item Bought**",value="** :card_index: Premium Membership :card_index: **")
            pro.add_field(name="**Cost**",value=f"**20000** {gem}")
            
            await ctx.send(embed=pro)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (20000, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Bought Premium Membership", "-20000", time, ctx.author.id))
            db.commit()		
            
            
            cursor.execute("UPDATE economy SET premium = ? WHERE user_id = ?", ("enabled", ctx.author.id))
            db.commit()
            return




    @buy.command()
    async def meme(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            chk = discord.Embed(title=f"**You Are Not Registered!**", color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=chk)
            return
            
        mem = cursor.execute(f"SELECT meme FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if mem[0] == "enabled":
            pmem= discord.Embed(title=f"You Have Already Bought Premium Meme Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=pmem)
            return
            
        premo = cursor.execute(f"SELECT premium FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if premo[0] == "disabled":
            pmem= discord.Embed(title=f"You Are Not Having Premium Membership To Buy This Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=pmem)
            return
            
        wallio = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if wallio[0] < 4000:
            noi = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Buy Premium Meme Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noi)
            return
            
        if mem[0] == "disabled":
            prop = discord.Embed(title=f"{tada} Transaction Was Successful! {tada}",color=0x00ff00, timestamp=ctx.message.created_at)
            
            prop.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            prop.add_field(name="**Item Bought**",value="**Premium Meme Command**")
            prop.add_field(name="**Cost**",value=f"**4000** {gem}")
            
            await ctx.send(embed=prop)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (4000, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Bought Premium Meme Command", "-4000", time, ctx.author.id))
            db.commit()		
            
            
            cursor.execute("UPDATE economy SET meme = ? WHERE user_id = ?", ("enabled", ctx.author.id))
            db.commit()
            return




    @buy.command()
    async def insult(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            chk = discord.Embed(title=f"**You Are Not Registered!**", color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=chk)
            return
            
        ins = cursor.execute(f"SELECT insult FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if ins[0] == "enabled":
            pmem= discord.Embed(title=f"You Have Already Bought Premium Insult Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=pmem)
            return
            
        premo = cursor.execute(f"SELECT premium FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if premo[0] == "disabled":
            pmem= discord.Embed(title=f"You Are Not Having Premium Membership To Buy This Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=pmem)
            return
            
        wallio = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if wallio[0] < 8000:
            noi = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Buy Premium Meme Command!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=noi)
            return
            
        if ins[0] == "disabled":
            prop = discord.Embed(title=f"{tada} Transaction Was Successful! {tada}",color=0x00ff00, timestamp=ctx.message.created_at)
            
            prop.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            prop.add_field(name="**Item Bought**",value="**Premium Insult Command**")
            prop.add_field(name="**Cost**",value=f"**8000** {gem}")
            
            await ctx.send(embed=prop)
            
            cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (8000, ctx.author.id))
            db.commit()
            
            time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Bought Premium Insult Command", "-8000", time, ctx.author.id))
            db.commit()
            
            
            cursor.execute("UPDATE economy SET insult = ? WHERE user_id = ?", ("enabled", ctx.author.id))
            db.commit()
            return


def setup(bot):
	bot.add_cog(buy(bot))