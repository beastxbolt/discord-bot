import discord
from discord.ext import commands
import asyncio
import json
from botprefix import prefix


class nick(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	@commands.has_permissions(manage_nicknames = True)
	async def nick(self,ctx,member : discord.Member = None,*, name = None):

		try:
		
			if not member:
				em2 = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}nick [user] [new nickname]``", colour=0x0000FF, timestamp=ctx.message.created_at)
				await ctx.send(embed=em2)
				return
				
			if not name:
				await ctx.send("Please specify the new nickname which you want to keep!", delete_after=5)
				return
				
			else:
				emni = discord.Embed(title=f"{member}'s nickname has been Changed Succesfully!",colour=0x0000FF,timestamp=ctx.message.created_at)
				emni.add_field(name="Mod/Admin",value=f"{ctx.author.name}")
				emni.add_field(name=f"New Nickname",value=name)
				await member.edit(nick=name)
				await ctx.send(embed=emni)
				return
		except:
			ade = discord.Embed(title=f"I Can't Change That User's Nickname!",description="I Can't Change Nickname Of A User Having Higher Role Than Me!",colour=0x0000FF,timestamp=ctx.message.created_at)
			await ctx.send(embed=ade)
			return


def setup(bot):
	bot.add_cog(nick(bot))