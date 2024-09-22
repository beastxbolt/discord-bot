import discord
from discord.ext import commands
import asyncio


class serverinfo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def serverinfo(self, ctx):
		
		embed = discord.Embed(title=f"{ctx.guild.name} - Server Information", colour=0xFFFFF, timestamp=ctx.message.created_at)
		embed.add_field(name="**Name:**", value=ctx.guild.name, inline=True)		
		embed.add_field(name="**ID:**",value=ctx.guild.id, inline=True)	
		embed.add_field(name="**Region:**",value=str(ctx.guild.region).title(), inline=True)	
		embed.add_field(name="**Verification Level:**",value=ctx.guild.verification_level, inline=True)
		embed.add_field(name="**Owner:**", value=ctx.guild.owner.display_name, inline=True)
		embed.add_field(name="**Shard ID:**", value=ctx.guild.shard_id, inline=True)
		embed.add_field(name="**Created On:**", value=ctx.guild.created_at.strftime("%d/%m/%y %H:%M:%S"), inline=True)
		embed.add_field(name="**Most Recent Member:**", value=[member for member in ctx.guild.members if member.joined_at is max([member.joined_at for member in ctx.guild.members])][0].display_name, inline=True)
		embed.add_field(name="**Most Recent Joined At:**", value=max([member.joined_at for member in ctx.guild.members]).strftime("%d/%m/%y %H:%M:%S"), inline=True)
		embed.add_field(name="**Number of Members:**", value=len(ctx.guild.members), inline=True)
		embed.add_field(name="**Number of Humans:**", value=len([member for member in ctx.guild.members if not member.bot]), inline=True)
		embed.add_field(name="**Number of Bots:**", value=len([member for member in ctx.guild.members if member.bot]), inline=True)
		embed.add_field(name="**Number of Banned Members:**", value=len(await ctx.guild.bans()), inline=True)
		embed.add_field(name="**Number of Categories:**", value=len(ctx.guild.categories), inline=True)
		embed.add_field(name="**Total Number of Channels:**", value=len(ctx.guild.channels), inline=True)
		embed.add_field(name="**Number of Text Channels:**", value=len(ctx.guild.text_channels), inline=True)
		embed.add_field(name="**Number of Voice Channels:**", value=len(ctx.guild.voice_channels), inline=True)
		embed.add_field(name="**Number of Roles:**", value=len(ctx.guild.roles), inline=True)
		embed.add_field(name="**Number of Invites:**", value=len(await ctx.guild.invites()), inline=True)
		await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(serverinfo(bot))