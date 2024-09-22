import discord
from discord.ext import commands
import asyncio
import random
from random import choice
import json
import requests
import sqlite3
from sqlite3 import connect
from botprefix import prefix


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class insult(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	async def insult(self, ctx, member : discord.Member=None):

		result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()

		if result is None:
			e1m = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=e1m)
			return

		check = cursor.execute(f"SELECT insult FROM economy WHERE user_id = {ctx.author.id}").fetchone()

		if check[0] == "disabled":
			ins = discord.Embed(title="You Haven't Bought Premium Insult Command From The Shop!", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=ins)
			return


		if not member:
			nem = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}insult [user]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=nem)
			return
			
		else:
			
			apis = [f"https://insult.mattbas.org/api/insult.txt?who={member.name}", "https://evilinsult.com/generate_insult.php?lang=en&type=text"]
			
			r = requests.get(random.choice(apis))
			insult = r.text
			ins = discord.Embed(title=f"{member}", description=insult, colour=0x00ff1f, timestamp=ctx.message.created_at,)
			await ctx.send(embed=ins)
			return


def setup(bot):
	bot.add_cog(insult(bot))