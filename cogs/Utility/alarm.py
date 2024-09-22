import discord
from discord.ext import commands
import asyncio
from asyncio import sleep
import json
import random
from random import choice
from botprefix import prefix


class alarm(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	
	@commands.command()
	async def alarm(self, ctx, dur : int = 0, *, reminder : str = None):
		
		l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
		
		a = random.choice(l)
		
		if not dur:
			ee = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}alarm [time(in min)] [reminder]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=ee)
			return
			
		if not reminder:
			await ctx.send("Please specify the reason why you want to set alarm!")
			return
			
		else:
			e = discord.Embed(title="⏰ Your Alarm Has Been Set! ⏰",colour=a,timestamp=ctx.message.created_at)
			e.set_author(name=ctx.author)
			
			await ctx.send(embed=e)
			
			await asyncio.sleep(dur*60)
			
			eee = discord.Embed(title="⏰ **Alarm** ⏰",colour=a, timestamp=ctx.message.created_at)
			eee.add_field(name="**Your Reminder:**",value=reminder)
			
			await ctx.author.send(embed=eee)


def setup(bot):
	bot.add_cog(alarm(bot))