import discord
from discord.ext import commands
import asyncio
import json
from botprefix import prefix

class slap(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def slap(self, ctx, member : discord.Member = None,*,reason = None):
		if not member:
			not_member = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}slap [user] [reason]``", colour=ctx.author.color, timestamp=ctx.message.created_at)
			await ctx.send(embed=not_member)
			return
			
		if not reason:
			await ctx.send("Please specify why you want to slap a user!", delete_after=5)
			return
			
		else:
			slapem = discord.Embed(title=f"{member} has been slapped by {ctx.author.name}",colour=ctx.author.color,timestamp=ctx.message.created_at)
			slapem.add_field(name="Reason",value=reason)
			await ctx.send(embed=slapem)



def setup(bot):
	bot.add_cog(slap(bot))