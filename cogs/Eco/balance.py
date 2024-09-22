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



class balance(commands.Cog):
	def __init__(self,bot):
		self.bot = bot


	@commands.command(aliases=['bal'])
	async def balance(self,ctx):
		
		gem = self.bot.get_emoji(710105510984286238)
		tada = self.bot.get_emoji(709752857653673994)
		loading = self.bot.get_emoji(710075331725361272)
		
		try:

			result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()

			if result is None:
				e1m = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=e1m)
				return

			else:
				wall = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
						
				walle = discord.Embed(title=f"{ctx.author}'s Wallet!",description=f"You Have **{wall[0].__repr__()}** {gem} in your wallet! {tada}",colour=0xFFFF00,timestamp=ctx.message.created_at)
						
				await ctx.send(embed=walle)
				return
		except Exception as e:
			print(e)



def setup(bot):
	bot.add_cog(balance(bot))