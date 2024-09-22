import discord
from discord.ext import commands
import asyncio
from botprefix import prefix


class mute(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def mute(self, ctx, member: discord.Member = None, *, reason = None):

		loading = self.bot.get_emoji(710075331725361272)

		if not member:
			embed = discord.Embed(title=f"This Commadnd Is Used Like This: ``{prefix(self.bot, ctx)[0]}mute [user] [reason(optional)]``", colour=ctx.author.color, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)
			return
			
		if member.bot == True:
			embed2 = discord.Embed(title=f"You cannot Mute Bots!", colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed2)
			return
			
		if member == ctx.author:
			embed3 = discord.Embed(title=f"You can't Mute Yourself!",colour=0xff0000, timestamp=ctx.message.created_at)
			await ctx.send(embed=embed3)
			return
			
		if member.guild_permissions.administrator:
				embed4 = discord.Embed(title=f"You can't Mute an Admin!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed4)
				return
				
		for role in member.roles:
			if role.name == "8-BIT Muted":
				embed5 = discord.Embed(title=f"{member} is already Muted!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed5)
				return
				
			guild = ctx.guild
			
			embed6 = discord.Embed(title=f"{member} has been Muted Successfully!🔇",colour=0x0000ff, timestamp=ctx.message.created_at)
			embed6.add_field(name="Mod/Admin",value=ctx.author,inline=False)
			embed6.add_field(name="Reason",value=reason,inline=False)
			
		async def addrole():
			guild = ctx.guild
			for role in guild.roles:
				if role.name == '8-BIT Muted':
					await member.add_roles(role)
					await msg.edit(embed=embed6)
					return


		for role in guild.roles:
			if role.name == '8-BIT Muted':
				await member.add_roles(role)
				await ctx.send(embed=embed6)
				return

			else:
				perms = discord.Permissions(administrator=False, view_audit_log=False, manage_guild=False, manage_roles=False, manage_channels=False, kick_members=False, ban_members=False, create_instant_invite=True, change_nickname=True, manage_nicknames=False, manage_webhooks=False, send_messages=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=True, use_external_emojis=False, add_reactions=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
				embed7 = discord.Embed(title=f"{loading} Looks Like 8-BIT Muted Role Was Deleted!\nPlease wait...",colour=0x00ff000,timestamp=ctx.message.created_at)
		msg = await ctx.send(embed=embed7)

		await guild.create_role(name="8-BIT Muted", colour=discord.Colour.from_rgb(1, 1, 1) , mentionable=False, permissions=perms)
		await asyncio.sleep(1)

		role2 = discord.utils.get(guild.roles, name="8-BIT Muted")

		for channel in ctx.guild.text_channels:
			
			perms = channel.overwrites_for(role2)
			perms.create_instant_invite = True
			perms.manage_channels = False
			perms.manage_permissions = False
			perms.manage_webhooks = False
			perms.read_messages = True
			perms.send_messages = False
			perms.send_tts_messages = False
			perms.manage_messages = False
			perms.embed_links = False
			perms.attach_files = False
			perms.read_message_history = True
			perms.use_external_emojis = False
			perms.add_reactions = False
			await channel.set_permissions(role2, overwrite=perms)
			
		role3 = discord.utils.get(guild.roles, name="8-BIT Muted")
		
		for channel in ctx.guild.voice_channels:
			
			perms2 = channel.overwrites_for(role3)
			perms2.create_instant_invite = True
			perms2.manage_channels = False
			perms2.manage_permissions = False
			perms2.manage_webhooks = False
			perms2.view_channel = True
			perms2.connect = False
			perms2.speak = False
			perms2.stream = False
			perms2.mute_members = False
			perms2.deafen_members = False
			perms2.move_members = False
			perms2.use_voice_activation = False
			perms2.priority_speaker = False
			await channel.set_permissions(role3, overwrite=perms2)

		await addrole()



def setup(bot):
	bot.add_cog(mute(bot))