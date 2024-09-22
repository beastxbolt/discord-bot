import discord
from discord.ext import commands
import asyncio
from botprefix import prefix

class unmute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
			
	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def unmute(self, ctx, member: discord.Member = None, reason = None):
		if not member:
			embed = discord.Embed(title=f"This Command I Used Like This: ``{prefix(self.bot, ctx)[0]}unmute [user]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return
			
		if member.bot == True:
			embed2 = discord.Embed(title=f"Bots were Never Muted!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed2)
			return
			
		if member == ctx.author:
			embed3 = discord.Embed(title=f"You were Never Muted!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed3)
			return
			
		if member.guild_permissions.administrator:
			embed4 = discord.Embed(title=f"Admins were Never Muted!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed4)
			return
		
		for role in member.roles:
			if role.name == "8-BIT Muted":
				embed5 = discord.Embed(title=f"{member} has been successfully Unmuted!🔊",colour=0x00ff00, timestamp=ctx.message.created_at)
				embed5.add_field(name="Mod/Admin", value=ctx.author.name,inline=False)
				embed5.add_field(name="Reason", value=reason,inline=False)
				await member.remove_roles(role)
				await ctx.send(embed=embed5)
				return
		else:
			embed6 = discord.Embed(title=f"{member} was Never Muted!",colour=0xff0000,timestamp=ctx.message.created_at)
			await ctx.send(embed=embed6)
			return


def setup(bot):
	bot.add_cog(unmute(bot))