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
from botprefix import prefix


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()

class gift(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def gift(self,ctx, member : discord.Member = None,*,amount : int=None):
	
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        if not member:
            emm = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}gift [user] [amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=emm)
            return
            
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {member.id}").fetchone()

        if result is None:
            em = discord.Embed(title=f"**The Specified User Is Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=em)
            return
            
        else:
            if amount <= 0:
                await ctx.send("Please specify gift amount greater than 0!", delete_after=5)
                return
                
            if amount > 0:
                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (amount, member.id))
                db.commit()
                
                e = discord.Embed(title=f"{loading} Sending Gift To The User! Please wait...", colour=0x00ff00)
                
                ee = discord.Embed(title=f"{tada} **I Have Sent The Gift!** {tada}",colour=0x00ff00,timestamp=ctx.message.created_at)
                
                ee.add_field(name="**Amount**", value=f"{amount} {gem}")
                
                ee.add_field(name="**Gift Sent To**", value=member)
                
                ee.set_thumbnail(url=self.bot.user.avatar_url)
                
                msg = await ctx.send(embed=e)
                await asyncio.sleep(3)
                await msg.edit(embed=ee)
                
                
                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Gift Received", "+" + f"{amount}", time, member.id))
                db.commit()
            return



def setup(bot):
	bot.add_cog(gift(bot))