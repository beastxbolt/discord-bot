import discord
from discord.ext import commands
import asyncio
import sqlite3
from sqlite3 import connect
import json
from botprefix import prefix

db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()

class warnlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def warnlog(self, ctx, member : discord.Member = None):

        if not member:
            embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}warnlog [user]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        checkWarnings = cursor.execute(f"SELECT warning FROM warnlog WHERE user_id = {member.id} AND guild_id = {member.guild.id}").fetchone()

        if checkWarnings is None:
            embed2= discord.Embed(title=f"No Warnings Found For The Specified User!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return

        else:
            warnings = cursor.execute(f"SELECT * FROM warnlog WHERE user_id = {member.id} ORDER BY id DESC LIMIT 10").fetchall()

            var = 1
            embed3 = discord.Embed(title=f":warning: Warnlog Of {member} :warning:",color=0xffa500,timestamp=ctx.message.created_at)
            embed3.set_thumbnail(url=member.avatar_url)

            for w in warnings:
                embed3.add_field(name=f"**`#{var}` At {w[5]} By {self.bot.get_user(w[3])}**", value=f"**Reason - {w[4]}!**", inline=False)
                var += 1

            await ctx.send(embed=embed3)
    

def setup(bot):
	bot.add_cog(warnlog(bot))
