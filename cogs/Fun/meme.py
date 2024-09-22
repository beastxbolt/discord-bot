import discord
from discord.ext import commands
import asyncio
import random
import requests
import sqlite3
from sqlite3 import connect

db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()

class meme(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def meme(self, ctx):

		result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()

		if result is None:
			e1m = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=e1m)
			return

		check = cursor.execute(f"SELECT meme FROM economy WHERE user_id = {ctx.author.id}").fetchone()

		if check[0] == "disabled":
			embed = discord.Embed(title="You Haven't Bought Premium Meme Command From The Shop!", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return

		else:
			url = "https://apis.duncte123.me/meme"
			meme = requests.get(url)
			json_meme = meme.json()
			meme_data = json_meme["data"]
			meme_title = meme_data["title"]
			meme_link = meme_data["image"]
			
			l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
			a = random.choice(l)
			e = discord.Embed(title=meme_title,colour = a,timestamp=ctx.message.created_at)
			e.set_image(url=f"{meme_link}")
			await ctx.send(embed=e)



def setup(bot):
	bot.add_cog(meme(bot))