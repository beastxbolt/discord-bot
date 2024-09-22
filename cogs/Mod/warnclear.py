import discord
from discord.ext import commands
import asyncio
import sqlite3
from sqlite3 import connect
import json
from botprefix import prefix

db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()

class warnclear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def warnclear(self, ctx, member : discord.Member = None):

        if not member:
            embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}warnclear [user]``", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        checkWarnings = cursor.execute(f"SELECT warning FROM warnlog WHERE user_id = {member.id} AND guild_id = {member.guild.id}").fetchone()

        if checkWarnings is None:
            embed2= discord.Embed(title=f"No Warnings Found For The Specified User!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return
        
        else:
            cursor.execute("DELETE FROM warnlog WHERE user_id = ? AND guild_id = ?", (member.id, member.guild.id))
            db.commit()

            embed3 = discord.Embed(title=f":warning: Cleared All Warnings For {member} :warning:",color=0x00ff00,timestamp=ctx.message.created_at)
            embed3.add_field(name="Mod/Admin", value=f"**{ctx.author}**")
            await ctx.send(embed=embed3)
            return
    

def setup(bot):
	bot.add_cog(warnclear(bot))
