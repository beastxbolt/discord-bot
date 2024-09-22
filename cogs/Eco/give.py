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


class give(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	async def give(self,ctx, member : discord.Member = None,*, amount : int = None):
	
		gem = self.bot.get_emoji(710105510984286238)
		tada = self.bot.get_emoji(709752857653673994)
		loading = self.bot.get_emoji(710075331725361272)
		
		result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
		
		
		if not member:
			e8m = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}give [user] [amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=e8m)
			return
			
		if result is None:
			em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=em)
			return
			
		mem = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {member.id}").fetchone()
			
		if mem is None:
			eem = discord.Embed(title=f"**The Specified User Is Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=eem)
			return
			
		if amount is None:
			await ctx.send(f"Please specify the amount of {gem} you want to give!", delete_after=5)
			return 
			
		if amount <= 0:
			await ctx.send("Please specify the amount you want to give greater than **0**!", delete_after=5)
			return
			
		wall = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
		
		if amount <= wall[0]:
			cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
			db.commit()
			
			time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
			cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", (f"Gifted Amount To {member}", "-" + f"{amount}", time, ctx.author.id))
			db.commit()
			
			
			
			cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (amount, member.id))
			db.commit()
			
			time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
			cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", (f"Gift Received From {ctx.author}", "-" + f"{amount}", time, member.id))
			db.commit()
			
			
			
			ee = discord.Embed(title=f"{tada} Transaction Was Successful! {tada}",colour=0x00ff00,timestamp=ctx.message.created_at)
			ee.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
			
			ee.add_field(name="**Amount**",value=f"{amount} {gem}")
			
			ee.add_field(name="**Given By**",value=ctx.author)
			
			ee.add_field(name="**Given To**",value=member)
			
			await ctx.send(embed=ee)
			return
			
		else:
			noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Give Others!", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=noe)
			return


def setup(bot):
	bot.add_cog(give(bot))