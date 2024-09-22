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


class bank(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def bank(self,ctx):
        
        gem = self.bot.get_emoji(710105510984286238)
        tada = self.bot.get_emoji(709752857653673994)
        loading = self.bot.get_emoji(710075331725361272)
        
        result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
        
        if result is None:
            e1m = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=e1m)
            return
            
        else:
            bankk = cursor.execute(f"SELECT bank FROM economy WHERE user_id = {ctx.author.id}").fetchone()
            
            banke = discord.Embed(title=f"{ctx.author}'s Bank!",description=f":bank: You Have **{bankk[0].__repr__()}** {gem} in your bank account! {tada}",colour=0x0000FF,timestamp=ctx.message.created_at)
            
            await ctx.send(embed=banke)
            return


def setup(bot):
	bot.add_cog(bank(bot))