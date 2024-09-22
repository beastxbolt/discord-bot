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


class profile(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def profile(self,ctx):
        
        try:
            
            result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
            
            if result is None:
                chk = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=chk)
                return
            
            else:
                image = Image.open('./Assets/profile.png')
                
                draw = ImageDraw.Draw(image)
                
                AVATAR_SIZE = 256
                
                avatar_asset = ctx.author.avatar_url_as(format='png', size=AVATAR_SIZE)
                
                buffer_avatar = io.BytesIO()
                
                await avatar_asset.save(buffer_avatar)
                
                buffer_avatar.seek(0)
                
                avatar_image = Image.open(buffer_avatar)
                
                avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
                
                circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
                circle_draw = ImageDraw.Draw(circle_image)
                circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
                avatar_image.putalpha(circle_image)
                avatar_image.show()
            
                
                image.paste(avatar_image, (784, 424), circle_image)
                
                font = ImageFont.truetype('./YourGone.ttf', 50)
                
                wall = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
                
                level = cursor.execute(f"SELECT level FROM experience WHERE user_id = {ctx.author.id} and guild_id = {ctx.author.guild.id}").fetchone()
                
                totalxp = cursor.execute(f"SELECT totalxp FROM experience WHERE user_id = {ctx.author.id} and guild_id = {ctx.author.guild.id}").fetchone()
                
                text = f"{ctx.author.id}"
                text2 = f"{ctx.author}"
                text3 = f"{wall[0].__str__()}"
                text4 = f"{totalxp[0].__str__()}"
                text5 = f"{level[0].__str__()}"
                
                
                draw.text((246, 65), text, fill=(255,255,255,255), font=font)
                
                draw.text((196,160), text2, fill=(255,255,255,255), font=font)
                
                draw.text((205,275), text3, fill=(255,255,255,255), font=font)
                
                draw.text((275,390), text4, fill=(255,255,255,255), font=font)
                
                draw.text((236,510), text5, fill=(255,255,255,255), font=font)
        
                buffer = io.BytesIO()
                image.save(buffer, format='png')
                
                buffer.seek(0)
                
                await ctx.send(file=discord.File(buffer, 'myimage.png'))
            
        except Exception as e:
            print(e)



def setup(bot):
	bot.add_cog(profile(bot))