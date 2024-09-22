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


class deposit(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(aliases=['dep'])
	async def deposit(self, ctx,*,amount : int = None):
		
		gem = self.bot.get_emoji(710105510984286238)
		tada = self.bot.get_emoji(709752857653673994)
		loading = self.bot.get_emoji(710075331725361272)
		
		result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()

		if result is None:
			em = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=em)
			return
			
		if result is not None:
			if amount is None:
				e8m = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}deposit [amount]``", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=e8m)
				return
				
			if amount < 0:
				await ctx.send("Please specify the amount to withdraw greater than **0**!", delete_after=5)
				return
				
			wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
			if amount <= wallet[0]:
				
				cursor.execute("UPDATE economy SET bank = bank + ? WHERE user_id = ?", (amount, ctx.author.id))
				db.commit()
				
				bank = cursor.execute(f"SELECT bank FROM economy WHERE user_id = {ctx.author.id}").fetchone()
				
				cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
				db.commit()
				
				e = discord.Embed(title=f"{loading} Processing Your Transaction! Please wait...",colour=0x00ff00)
				
				ets = discord.Embed(title=f"{tada} Transaction Was Successfull {tada}", description=f"**{amount}** {gem} Have Been Deposited In Your Bank! Your Updated Bank Balance Is **{bank[0].__repr__()}** {gem}",colour=0x0080ff,timestamp=ctx.message.created_at)
				ets.set_author(name=ctx.author)
				msg = await ctx.send(embed=e)
				await asyncio.sleep(3.0)
				await msg.edit(embed=ets)
				
				time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
				cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Deposited To Bank", "-" + f"{amount}", time, ctx.author.id))
				db.commit()
				return
				
			else:
				
				noe = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Deposit!", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=noe)
				return


def setup(bot):
	bot.add_cog(deposit(bot))