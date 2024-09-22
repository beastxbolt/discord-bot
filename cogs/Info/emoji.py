import discord
from discord.ext import commands
import asyncio
from asyncio import sleep
from botprefix import prefix

class emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def emoji(self, ctx, *, emoji : discord.Emoji = None):

        try:

            if emoji is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}emoji [emoji]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            else:
                embed2 = discord.Embed(title="Emoji Info",colour=0xf1c40f,timestamp=ctx.message.created_at)
                embed2.add_field(name="Emoji ID", value=emoji.id)
                embed2.add_field(name="Emoji Name", value=emoji.name)
                embed2.add_field(name="Animated", value=emoji.animated)
                embed2.set_image(url=emoji.url)
                await ctx.send(embed=embed2)
                return


        except:
            embed3 = discord.Embed(title="Invalid Emoji",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)
            return

        

def setup(bot):
	bot.add_cog(emoji(bot))