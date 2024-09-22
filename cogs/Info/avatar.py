import discord
from discord.ext import commands
import asyncio
import json
from botprefix import prefix


class avatar(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	async def avatar(self, ctx, member : discord.Member = None):
		if not member:
			embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}avatar [user]``", colour=0x3CB371, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return
			
		else:
			embed2 = discord.Embed(title=f"{member}'s avatar is below!",colour=0x3CB371,timestamp=ctx.message.created_at)
			embed2.add_field(name="Animated Avatar?",value=member.is_avatar_animated())
			embed2.set_image(url=member.avatar_url)
			await ctx.send(embed=embed2)
			return


def setup(bot):
	bot.add_cog(avatar(bot))