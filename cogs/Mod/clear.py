import discord
from discord.ext import commands
import asyncio


class clear(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(aliases=['purge'])
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount: int = 0):
		
		if amount <= 0:
			await ctx.send("Please Specify An Amount Greater Than 0!", delete_after = 5)
			
		elif amount > 100:
			await ctx.send("You Can't Delete More Than 100 Messages At Once!", delete_after = 5)
			
		elif amount >= 1:
			await ctx.message.delete()
			await ctx.channel.purge(limit=amount)
			await ctx.send("💬 I Have Deleted {} Messages!" .format(amount), delete_after = 5)



def setup(bot):
	bot.add_cog(clear(bot))