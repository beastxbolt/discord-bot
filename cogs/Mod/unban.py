import discord
from discord.ext import commands
import asyncio
from botprefix import prefix

class unban(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx,*, member=None):

		if member is None:
			embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}unban [username#tag]``",colour=0xff0000,timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return

		if member is not None:
			banned_users = await ctx.guild.bans()
			member_name, member_discriminator = member.split('#')
				
			for ban_entry in banned_users:
				user = ban_entry.user
					
				if (user.name, user.discriminator) == (member_name, member_discriminator):
						
					embed2 = discord.Embed(title=f"{member} Has Been Successfully Unbanned!",colour=0x00ff00,timestamp=ctx.message.created_at)
					embed2.add_field(name="Mod/Admin",value=ctx.author,inline=False)
					await ctx.guild.unban(user)
					await ctx.send(embed=embed2)
					return
			
			else:
				embed3 = discord.Embed(title=f"{member} Is Not Banned!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed3)




def setup(bot):
	bot.add_cog(unban(bot))