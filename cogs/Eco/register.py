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


class register(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def register(self,ctx):
	
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        if result is None:
            cursor.execute("INSERT INTO economy (user_id, wallet, bank, premium, meme, insult) VALUES (?,?,?,?,?,?)", (ctx.author.id, 1000, 0, "disabled","disabled","disabled"))
            db.commit()
            
            cursor.execute("INSERT INTO inventory (user_id, bread, cookie, candy, beer) VALUES (?,?,?,?,?)", (ctx.author.id, 0, 0, 0, 0))
            db.commit()
            
            wall_bal, bank_bal = cursor.execute(f"SELECT wallet, bank FROM economy WHERE user_id = {ctx.author.id}").fetchone()
            
            
            e = discord.Embed(title=f"{loading} Processing Your Request! Please wait...",colour=0x00ff00)	
            
            e9 = discord.Embed(title=f"{tada}**You Have Been Registered Successfully!**{tada}",colour=0x00ff00,timestamp=ctx.message.created_at)
            
            e9.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            
            e9.add_field(name="**Name**", value=ctx.author, inline=False)
            
            e9.add_field(name="**ID**", value=ctx.author.id, inline=False)
            
            e9.add_field(name="**Wallet Balance**", value=f"{wall_bal.__repr__()} {gem}", inline=False)
            
            e9.add_field(name="**Bank Balance**", value=f"{bank_bal.__repr__()} {gem}", inline=False)
            
            msg = await ctx.send(embed=e)
            await asyncio.sleep(4)
            await msg.edit(embed=e9)
            
            time = datetime.datetime.now().strftime("%d/%-m/%Y %-I:%-M:%S %p")
            cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Registration Bonus", "+1000", time, ctx.author.id))
            db.commit()
            return
            
        elif result is not None:
            enot = discord.Embed(title="**You Are Already Registered!**",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=enot)
            return



def setup(bot):
	bot.add_cog(register(bot))