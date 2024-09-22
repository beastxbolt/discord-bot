import discord
from discord.ext import commands
import asyncio
from random import choice, randrange



class com(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("Invite Link - **https://discord.com/api/oauth2/authorize?client_id=735700750767882300&permissions=8&scope=bot**")

    @commands.command(aliases=["shout"])
    async def say(self, ctx, *, text):
    	await ctx.message.delete()
    	await ctx.send(text)


def setup(bot):
    bot.add_cog(com(bot))
