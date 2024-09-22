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


class suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suggest(self, ctx, *, text : str = None):

        thumbs_up = '\U0001F44D'
        thumbs_down = '\U0001F44E'

        try:
            if text is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}suggest [suggestion]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            checkChannel = cursor.execute(f"SELECT channel_id FROM suggestion WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkChannel is None:
                embed2 = discord.Embed(title="Suggestion Channel Has Not Been Set Yet!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            checkStatus = cursor.execute(f"SELECT status FROM suggestion WHERE guild_id = {ctx.author.guild.id}").fetchone()

            if checkStatus[0] == "disabled":
                await ctx.send(f"{ctx.author.mention}, Suggest Command Is Disabled!")
                return

            suggestionchannel = self.bot.get_channel(id=checkChannel[0].__int__())

            if not suggestionchannel:
                embed3 = discord.Embed(title="Suggestion Channel Which Was Set Does Not Exist!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

            else:
                embed4 = discord.Embed(title=":notepad_spiral: New Suggestion!",description=text,colour=0x00ff86,timestamp=ctx.message.created_at)
                embed4.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
                embed4.set_footer(text=f"Suggestion By: {ctx.author.name}")
                await ctx.message.delete()

                msg = await suggestionchannel.send(embed=embed4)
                await msg.add_reaction(emoji = thumbs_up)
                await msg.add_reaction(emoji = thumbs_down)

                await ctx.send(f":white_check_mark: {ctx.author.mention}, Your Suggestion Has Been Posted!")
                return

        except Exception as e:
            print(e)



def setup(bot):
    bot.add_cog(suggest(bot))