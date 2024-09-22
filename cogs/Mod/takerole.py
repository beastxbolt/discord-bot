import discord
from discord.ext import commands
import asyncio
import json
import random
from random import choice
from botprefix import prefix

class takerole(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	
	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def takerole(self,ctx,member : discord.Member = None,*, role : str = None):
		l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
		a = random.choice(l)
		
		if not member:
			e = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}takerole [user] [role]``",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=e)
			return
			
		if member == ctx.author:
			ctem = discord.Embed(title=f"You can't remove roles from Yourself!",colour=a, timestamp=ctx.message.created_at)
			await ctx.send(embed=ctem)
			return
			
		if member.bot == True:
			botme = discord.Embed(title=f"You can't remove roles from Bots!",colour=member.color,timestamp=ctx.message.created_at)
			await ctx.send(embed=botme)
			return
			
		embd = discord.Embed(title="I can't remove roles from Mod/Admin!",colour=a,timestamp=ctx.message.created_at)
			
		if member.guild_permissions.administrator:
			await ctx.send(embed=embd)
			return
			
		if not role:
			e = discord.Embed(title=f"Give me a role name to remove from the Member!",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=e)
			return
				
		for roless in member.roles:
			if roless.name == role:
				await member.remove_roles(roless)
				embed = discord.Embed(title=f"{role} role has been removed from {member}!",colour=a,timestamp=ctx.message.created_at)
				embed.add_field(name="Mod/Admin",value=ctx.author)
				await ctx.send(embed=embed)
				return
				
		else:
			emb1 = discord.Embed(title=f"{member} doesn't have a role with {role} name!",colour=a,timestamp=ctx.message.created_at)
			await ctx.send(embed=emb1)
			return


def setup(bot):
	bot.add_cog(takerole(bot))