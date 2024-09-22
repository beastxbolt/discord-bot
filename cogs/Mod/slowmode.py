import discord
from discord.ext import commands
import asyncio
from asyncio import TimeoutError
import json
from botprefix import prefix


class slowmode(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command(aliases=['sm'])
	@commands.has_permissions(manage_channels = True)
	async def slowmode(self, ctx, delay : int = None):
		tick = '\U00002705'
		cross = '\U0000274E'
		
		if delay == None:
			emb = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}slowmode [time(in sec)]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=emb)
			return
			
		if delay > 21600:
			await ctx.send("Please specify slowmode time (in sec) less than 21601 seconds!")
			return
			
		else:
			ee = discord.Embed(title=f"Do you want to set **{delay}** seconds slowmode time for this channel?", colour=0x00ff00, timestamp=ctx.message.created_at)
			
			msg = await ctx.send(embed=ee)
			await msg.add_reaction(emoji = tick)
			await msg.add_reaction(emoji = cross)
			
			eee = discord.Embed(title=f"**{delay}** seconds slowmode time has been set for this channel!",colour=0x00ff00,timestamp=ctx.message.created_at)
			
		def check(reaction, user):
			return not user.bot and user.id == ctx.author.id
			
		try:
			reaction, user = await self.bot.wait_for('reaction_add', timeout=120, check=check)
			
			if reaction.emoji == tick:
				await ctx.channel.edit(slowmode_delay=delay)
				await msg.edit(embed=eee)
				
			elif reaction.emoji == cross:
				await msg.delete()
				
		except asyncio.TimeoutError:
			await msg.delete()
			await ctx.send('Timed out!', delete_after =5)



def setup(bot):
	bot.add_cog(slowmode(bot))