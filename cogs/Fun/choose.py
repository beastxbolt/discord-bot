import discord
from discord.ext import commands
import asyncio
import random
from random import choice
import json
from botprefix import prefix


class choose(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def choose(self,ctx,word1 = None,word2 = None):
		if not word1:
			e = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}choose [choice1] [choice2]``",colour=discord.Colour.dark_teal(),timestamp=ctx.message.created_at)
			e.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
			e.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=e)
			return
			
		if not word2:
			e = discord.Embed(title="Give me 2 words to choose from!",colour=discord.Colour.dark_teal(),timestamp=ctx.message.created_at)
			e.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
			e.set_footer(text=self.bot.user.name,icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=e)
			return
			
		else:
			l = [word1,word2,word1,word2]
			a = random.choice(l)
			await ctx.send(f"I choose {a}")



def setup(bot):
	bot.add_cog(choose(bot))