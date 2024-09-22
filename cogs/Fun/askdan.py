import discord
from discord.ext import commands
import asyncio
import json
import random
from botprefix import prefix

answers = ["Absolutely Yes!", "Better not tell you now!", "I don't know!", "Maybe...", "That's a secret, I can't share my secrets to a fool!", "I have no idea about it!", "No way!", "Nope", "Ask again later!", "Yes", "No Never", "Definitely Yes", "You may rely on it!", "Yes Of Course!", "Can't predict now!", "Without a doubt!", "You asked such a fool question!", "Concentrate and ask again!", "It's very doubtful!", "My sources say no!", "Most likely, Yes!"]
img = random.choice(['DanSad', 'DanHappy'])

class askdan(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	async def askdan(self, ctx,*, question : str = None):

		try:
			
			if question is None:
				ques = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}askdan [question]``", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=ques)
				return
				
			else:
				file = discord.File(f'./Assets/{img}.png', filename='img.png')
				emb = discord.Embed(title=f"{ctx.author.display_name} asked Dan a question!", colour=0x00ff00,timestamp=ctx.message.created_at)
				emb.add_field(name="**Question**",value=question, inline=True)
				emb.add_field(name="**Dan's Reply**",value=(random.choice(answers)),inline=True)
				emb.set_thumbnail(url=f'attachment://{img}.png')
				
				await ctx.send(embed=emb)

		except Exception as e:
			print(e)



def setup(bot):
	bot.add_cog(askdan(bot))