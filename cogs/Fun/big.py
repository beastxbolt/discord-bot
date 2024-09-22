import discord
from discord.ext import commands
import asyncio
from pyfiglet import figlet_format, FontNotFound
import json
from botprefix import prefix


class big(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def big(self, ctx,*, text=None):
		if not text:
			tex = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}big [text]``", colour=0x3CB371, timestamp=ctx.message.created_at)
			await ctx.send(embed=tex)
			return
			
		else:
			await ctx.send("```fix\n" + figlet_format(text, font="big") + "```")


def setup(bot):
	bot.add_cog(big(bot))