import discord
from discord.ext import commands
import asyncio
from botprefix import prefix


class mention(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def mention(self, ctx, role : str = None):

		if role is None:
			embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}mention [role]``",colour=0xff0000,timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return

		if role is not None:
			for roles in ctx.author.guild.roles:
				if roles.name == role:
					await ctx.message.delete()
					await ctx.send(roles.mention)
					return

			else:
				embed2 = discord.Embed(title="No Such Role Found!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed2)
				return




def setup(bot):
	bot.add_cog(mention(bot))