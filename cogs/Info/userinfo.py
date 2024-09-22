import discord
from discord.ext import commands
import asyncio


class userinfo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def userinfo(self, ctx, member: discord.Member = None):
		
		permList = []

		if member is None:
			member = ctx.author
			roles = [role for role in ctx.author.roles]
		else:
			roles = [role for role in member.roles]
			
		for perm in member.guild_permissions:
			if perm[1] is True:
				permList.append(perm[0])

		embed = discord.Embed(title=f"{member}", colour=member.color, timestamp=ctx.message.created_at)
		embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
		embed.set_author(name="User Info: ")
		embed.add_field(name="ID:", value=member.id, inline=False)
		embed.add_field(name="User Name:",value=member.display_name, inline=False)
		embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
		embed.add_field(name="Current Status:",value=str(member.status).title(), inline=False)
		embed.add_field(name="Current Activity:",value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
		embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I: %M %p UTC"), inline=False)
		embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I: %M %p UTC"), inline=False)
		embed.add_field(name=f"Roles [{len(roles)}]:", value=" **|** ".join([role.mention for role in roles]), inline=False)
		embed.add_field(name="Top Role:",value=member.top_role, inline=False)
		embed.add_field(name=f"Permissions:", value=", ".join([perm for perm in permList]), inline=False)
		embed.add_field(name="Bot?:", value=member.bot, inline=False)
		await ctx.send(embed=embed)
		return


def setup(bot):
	bot.add_cog(userinfo(bot))