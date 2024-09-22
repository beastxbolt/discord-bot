import discord
from discord.ext import commands
import asyncio
from asyncio import sleep


class ping(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def ping(self, ctx, dur : int = 0.5):
		msg = await ctx.send(f"📡 Checking my ping")
		await msg.edit(content="📡 Checking my ping")
		await asyncio.sleep(dur)
		await msg.edit(content="📡 Checking my ping.")
		await asyncio.sleep(dur)
		await msg.edit(content="📡 Checking my ping..")
		await asyncio.sleep(dur)
		await msg.edit(content="📡 Checking my ping...")
		await asyncio.sleep(dur)
		await msg.edit(content=f"📡 My ping - {round(self.bot.latency * 1000)}ms 📡")


def setup(bot):
	bot.add_cog(ping(bot))