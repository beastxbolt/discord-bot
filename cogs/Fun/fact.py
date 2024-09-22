import discord
from discord.ext import commands
import asyncio
import random
import requests


class fact(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def fact(self, ctx):

		url = "https://nekos.life/api/v2/fact"
		fact = requests.get(url)
		json_fact = fact.json()
		fact_data = json_fact["fact"]
			
		colours = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
		a = random.choice(colours)
		embed = discord.Embed(title=":notepad_spiral: Random Fact", description=fact_data ,colour = a,timestamp=ctx.message.created_at)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(fact(bot))