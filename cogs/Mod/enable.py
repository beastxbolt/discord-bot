import discord
from discord.ext import commands
import asyncio
import sqlite3
from sqlite3 import connect

db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class enable(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.group()
    @commands.has_permissions(manage_channels = True)
    async def enable(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}enable [group|command|other]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return
            
    @enable.command()
    async def leveling(self, ctx):

        try:

            checkStatus = cursor.execute(f"SELECT status FROM config_leveling WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkStatus is None:
                await ctx.send(f"{ctx.author.mention}, Leveling System Is Already Enabled!")
                return

            if checkStatus[0] == "disabled":
                cursor.execute("UPDATE config_leveling SET status = ? WHERE guild_id = ?", ("enabled", ctx.author.guild.id))
                db.commit()

                await ctx.send(f"{ctx.author.mention}, Leveling System Has Been Enabled!")
                return

            if checkStatus[0] == "enabled":
                await ctx.send(f"{ctx.author.mention}, Leveling System Is Already Enabled!")
                return

        except Exception as e:
            print(e)


    @enable.command()
    async def suggest(self, ctx):

        try:

            checkStatus = cursor.execute(f"SELECT status FROM suggestion WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkStatus is None:
                await ctx.send(f"{ctx.author.mention}, Suggestion Channel Has Not Been Set Yet!")
                return

            if checkStatus[0] == "disabled":
                cursor.execute("UPDATE suggestion SET status = ? WHERE guild_id = ?", ("enabled", ctx.author.guild.id))
                db.commit()

                await ctx.send(f"{ctx.author.mention}, Suggestion Has Been Enabled!")
                return

            if checkStatus[0] == "enabled":
                await ctx.send(f"{ctx.author.mention}, Suggestion Is Already Enabled!")
                return

        except Exception as e:
            print(e)


    @enable.command()
    async def welcome(self, ctx):

        try:

            checkStatus = cursor.execute(f"SELECT status FROM join_leave WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkStatus is None:
                await ctx.send(f"{ctx.author.mention}, Welcome Channel Has Not Been Set Yet!")
                return

            if checkStatus[0] == "disabled":
                cursor.execute("UPDATE join_leave SET status = ? WHERE guild_id = ?", ("enabled", ctx.author.guild.id))
                db.commit()

                await ctx.send(f"{ctx.author.mention}, Welcome Has Been Enabled!")
                return

            if checkStatus[0] == "enabled":
                await ctx.send(f"{ctx.author.mention}, Welcome Is Already Enabled!")
                return

        except Exception as e:
            print(e)


    @enable.command()
    async def invitelog(self, ctx):

        try:

            checkStatus = cursor.execute(f"SELECT status FROM invitation WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkStatus is None:
                await ctx.send(f"{ctx.author.mention}, Invite Log Channel Has Not Been Set Yet!")
                return

            if checkStatus[0] == "disabled":
                cursor.execute("UPDATE invitation SET status = ? WHERE guild_id = ?", ("enabled", ctx.author.guild.id))
                db.commit()

                await ctx.send(f"{ctx.author.mention}, Invite Log Has Been Enabled!")
                return

            if checkStatus[0] == "enabled":
                await ctx.send(f"{ctx.author.mention}, Invite Log Is Already Enabled!")
                return

        except Exception as e:
            print(e)



def setup(bot):
	bot.add_cog(enable(bot))