import discord
from discord.ext import commands
import asyncio
import random
from random import choice
import json
from botprefix import prefix


class giverole(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	@commands.has_permissions(manage_roles = True)
	async def giverole(self,ctx,member : discord.Member = None,*,role : str = None):
		l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
		a = random.choice(l)
		if not member:
			e = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}giverole [user] [role]``",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=e)
			return
			
		if member == ctx.author:
			ctem = discord.Embed(title=f"You can't give roles to Yourself!",colour=a, timestamp=ctx.message.created_at)
			await ctx.send(embed=ctem)
			return
			
		if not role:
			e = discord.Embed(title=f"Give me a role name to give the Member!",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=e)
			return
			
		for roless in member.roles:
			if roless.name == role:
				embed = discord.Embed(title=f"{member} already has {role} role!",colour=a,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed)
				return
				
		for roles in ctx.guild.roles:
			if roles.name == role:
				await member.add_roles(roles)
				embed = discord.Embed(title=f"{role} role has been given to {member}!",colour=a,timestamp=ctx.message.created_at)
				embed.add_field(name="Mod/Admin",value=ctx.author,inline=False)
				await ctx.send(embed=embed)
				return
				
		else:
			embed = discord.Embed(title=f"I coundn't find a role with {role} name!",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return


def setup(bot):
	bot.add_cog(giverole(bot))