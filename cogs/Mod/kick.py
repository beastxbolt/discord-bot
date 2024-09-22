import discord
from discord.ext import commands
import asyncio
from botprefix import prefix

class kick(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member = None, *, reason : str =None):
		
		if not member:
			n_mem = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}kick [user] [reason(optional)]``", colour=ctx.author.color, timestamp=ctx.message.created_at)
			await ctx.send(embed=n_mem)
			return
			
		if member.bot == True:
			botme = discord.Embed(title=f"You can't Kick Bots!",colour=member.color,timestamp=ctx.message.created_at)
			await ctx.send(embed=botme)
			return
			
		if member == ctx.author:
			emme = discord.Embed(title=f"You can't Kick Yourself!",colour=ctx.author.color,timestamp=ctx.message.created_at)
			await ctx.send(embed=emme)
			return
			
		if member.guild_permissions.administrator:
			stem = discord.Embed(title=f"You can't kick an Admin",colour=ctx.author.color,timestamp=ctx.message.created_at)
			await ctx.send(embed=stem)
			return
				
		if member:
			embed2 = discord.Embed(title=f"{member}  has been Kicked Successfully!",colour=ctx.author.color, timestamp=ctx.message.created_at)
			embed2.add_field(name="Mod/Admin", value=ctx.author, inline=False)
			embed2.add_field(name="Reason", value=reason, inline=False)
			await member.kick(reason=reason)
			await ctx.send(embed=embed2)
			return


def setup(bot):
	bot.add_cog(kick(bot))