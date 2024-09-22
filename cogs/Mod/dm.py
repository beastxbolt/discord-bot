import discord
from discord.ext import commands
import asyncio
from botprefix import prefix


class dm(commands.Cog):
	
	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def dm(self, ctx, member : discord.Member = None,*,txt = None):
		if not member:
			notm = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}dm [user] [message]``", colour=ctx.author.color, timestamp=ctx.message.created_at)
			await ctx.send(embed=notm)
			return
			
		if not txt:
			await ctx.send("Please type your message which you want to DM!")
			return
			
		else:
			dmed = discord.Embed(description=txt,colour=0x7b68ee,timestamp=ctx.message.created_at)
			await member.send(embed=dmed)
			
			done = discord.Embed(title=f"✅ DM Sent!",colour=0x32cd32,timestamp=ctx.message.created_at)
			await ctx.send(embed=done)
			return


def setup(bot):
	bot.add_cog(dm(bot))