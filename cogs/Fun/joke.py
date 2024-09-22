import discord
from discord.ext import commands
import asyncio
import random
from random import choice
import requests


class joke(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def joke(self, ctx):
		url = "https://official-joke-api.appspot.com/random_joke"
		joke = requests.get(url)
		json_joke = joke.json()
		joke_title = json_joke["setup"]
		joke_description = json_joke["punchline"]
		
		l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
		a = random.choice(l)
		e = discord.Embed(title=joke_title, description=joke_description,colour = a,timestamp=ctx.message.created_at)
		await ctx.send(embed=e)


def setup(bot):
	bot.add_cog(joke(bot))