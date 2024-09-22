import discord
from discord.ext import commands
import asyncio

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def roles(self, ctx):
        roles = [role for role in ctx.author.guild.roles]

        embed = discord.Embed(title=f"Server Roles Information\nNumber Of Roles : {len(roles)}",description=f" **|** ".join([role.mention for role in roles]),colour=0x00ff7f,timestamp=ctx.message.created_at)
        embed.set_footer(text=f"{ctx.author.guild}",icon_url=f"{ctx.author.guild.icon_url}")
        await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(roles(bot))