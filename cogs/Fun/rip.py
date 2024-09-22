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



class rip(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def rip(self,ctx, member : discord.Member=None):

        if not member:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}rip [user]``",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)

        else:
            try:
                
                image = Image.open('./Assets/rip.png')
                
                draw = ImageDraw.Draw(image)
                
                AVATAR_SIZE = 128
                
                avatar_asset = member.avatar_url_as(format='png', size=AVATAR_SIZE)
                
                buffer_avatar = io.BytesIO()
                
                await avatar_asset.save(buffer_avatar)
                
                buffer_avatar.seek(0)
                
                avatar_image = Image.open(buffer_avatar)
                
                avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
            
                
                image.paste(avatar_image, (66, 139))
                
                text = "2021-2022"
                
                font = ImageFont.truetype('./Arial.ttf', 30)
                draw.text( (60, 275), text, fill=(0,0,0), font=font)

                buffer = io.BytesIO()
                image.save(buffer, format='png')
                
                buffer.seek(0)
                
                await ctx.send(file=discord.File(buffer, 'myimage.png'))
                
            except Exception as e:
                print(e)



def setup(bot):
	bot.add_cog(rip(bot))