import discord
from discord.ext import commands
import asyncio
from botprefix import prefix


class ban(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member = None, *, reason=None):
		if not member:
			embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}ban [user] [reason(optional)]``", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			
		if member.bot == True:
			embed2 = discord.Embed(title=f"You can't Ban Bots!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed2)
			return
			
		if member == ctx.author:
			embed3 = discord.Embed(title="You can't Ban Yourself!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed3)
			return
			
		if member.guild_permissions.administrator:
			embed4 = discord.Embed(title="You can't ban an Admin!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed4)
			return
				
		else:
			embed5 = discord.Embed(title=f"{member}  has been Successfully Banned!",colour=0x0000ff, timestamp=ctx.message.created_at)
			embed5.add_field(name="Mod/Admin", value=ctx.author, inline=False)
			embed5.add_field(name="Reason", value=reason, inline=False)
			await member.ban(reason=reason)
			await ctx.send(embed=embed5)
			return  



def setup(bot):
	bot.add_cog(ban(bot))