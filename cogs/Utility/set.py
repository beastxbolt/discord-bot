import discord
from discord.ext import commands
import asyncio
import math
import random
from random import randrange
import sqlite3
from sqlite3 import connect
from botprefix import prefix


db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()


class set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def set(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}set [levelup|suggest|welcome]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


    @set.command()
    @commands.has_permissions(manage_channels = True)
    async def levelup(self, ctx, *, channel : discord.TextChannel = None):
        
        try:
            if channel is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}set levelup [channel]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            checkChannel = cursor.execute(f"SELECT channel_id FROM levelups WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkChannel is None:
                cursor.execute("INSERT INTO levelups (channel_id, guild_id) VALUES (?,?)", (channel.id, ctx.author.guild.id))
                db.commit()

                embed2 = discord.Embed(description=f"**Level Up Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            if checkChannel is not None:
                cursor.execute("UPDATE levelups SET channel_id = ? WHERE guild_id = ?", (channel.id, ctx.author.guild.id))
                db.commit()

                embed3 = discord.Embed(description=f"**Level Ups Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

        except Exception as e:
                print(e)
                
    
    @set.command()
    @commands.has_permissions(manage_channels = True)
    async def suggest(self, ctx, *, channel : discord.TextChannel = None):
        
        try:
            if channel is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}set suggest [channel]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            checkChannel = cursor.execute(f"SELECT channel_id FROM suggestion WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkChannel is None:
                cursor.execute("INSERT INTO suggestion (channel_id, guild_id, status) VALUES (?,?,?)", (channel.id, ctx.author.guild.id, "enabled"))
                db.commit()

                embed2 = discord.Embed(description=f"**Suggestion Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            if checkChannel is not None:
                cursor.execute("UPDATE suggestion SET channel_id = ? WHERE guild_id = ?", (channel.id, ctx.author.guild.id))
                db.commit()

                embed3 = discord.Embed(description=f"**Suggestion Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

        except Exception as e:
            print(e)


    @set.command()
    @commands.has_permissions(manage_channels = True)
    async def welcome(self, ctx, *, channel : discord.TextChannel = None):
        
        try:
            if channel is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}set welcome [channel]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            checkChannel = cursor.execute(f"SELECT channel_id FROM join_leave WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkChannel is None:
                cursor.execute("INSERT INTO join_leave (channel_id, guild_id, status) VALUES (?,?,?)", (channel.id, ctx.author.guild.id, "enabled"))
                db.commit()

                embed2 = discord.Embed(description=f"**Welcome Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            if checkChannel is not None:
                cursor.execute("UPDATE join_leave SET channel_id = ? WHERE guild_id = ?", (channel.id, ctx.author.guild.id))
                db.commit()

                embed3 = discord.Embed(description=f"**Welcome Messages Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

        except Exception as e:
            print(e)


    @set.command()
    @commands.has_permissions(manage_channels = True)
    async def invitelog(self, ctx, *, channel : discord.TextChannel = None):
        
        try:
            if channel is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}set invitelog [channel]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            checkChannel = cursor.execute(f"SELECT channel_id FROM invitation WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkChannel is None:
                cursor.execute("INSERT INTO invitation (channel_id, guild_id, status) VALUES (?,?,?)", (channel.id, ctx.author.guild.id, "enabled"))
                db.commit()

                embed2 = discord.Embed(description=f"**Invite Logs Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            if checkChannel is not None:
                cursor.execute("UPDATE invitation SET channel_id = ? WHERE guild_id = ?", (channel.id, ctx.author.guild.id))
                db.commit()

                embed3 = discord.Embed(description=f"**Invite Logs Will Be Redirected To {channel.mention}!**",colour=0x00ff00,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

        except Exception as e:
            print(e)



def setup(bot):
    bot.add_cog(set(bot))