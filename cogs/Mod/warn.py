import discord
from discord.ext import commands
import asyncio
import sqlite3
from sqlite3 import connect
import json
import datetime
from botprefix import prefix

db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()

class warn(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def warn(self, ctx, member : discord.Member = None, *,reason : str = None):
		try:

			if not member:
				embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}warn [user] [reason]``", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=embed)
				return

			if member == ctx.author:
				embed2 = discord.Embed(title=f"You can't Warn Yourself!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed2)
				return

			if member.bot == True:
					embed3 = discord.Embed(title=f"You can't Warn Bots!",colour=0xff0000,timestamp=ctx.message.created_at)
					await ctx.send(embed=embed3)
					return

			if member.guild_permissions.administrator:
				embed4 = discord.Embed(title=f"You can't Warn an Admin!",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed4)
				return


			if not reason:
					embed5 = discord.Embed(title="Please specify why you want to warn the user!", colour=0x0000ff, timestamp=ctx.message.created_at)
					await ctx.send(embed=embed5)
					return

			else:
				embed6 = discord.Embed(title=f"{member},  you were warned in {ctx.author.guild.name}!",colour=0x7b68ee,timestamp=ctx.message.created_at)
				embed6.add_field(name="Reason", value=reason, inline=False)
				embed6.set_author(name=member, icon_url=member.avatar_url)
				await member.send(embed=embed6)


				embed7 = discord.Embed(title=f"✅ {member} has been Warned!",colour=0x00ffff,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed7)

				time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
				cursor.execute("INSERT INTO warnlog (user_id, guild_id, warned_by, warning, time) VALUES (?,?,?,?,?)", (member.id, ctx.guild.id, ctx.author.id, reason, time))
				db.commit()
				return

		except Exception as e:
			print(e)


def setup(bot):
	bot.add_cog(warn(bot))
