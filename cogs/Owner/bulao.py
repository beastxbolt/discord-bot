import discord
import asyncio
from discord.ext import commands
from botprefix import prefix


class bulao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def bulao(self, ctx, guild_id : int = None):
        
        try:
            if guild_id is None:
                embed = discord.Embed(title="This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}bulao [guild_id]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)

            else:
                guild = self.bot.get_guild(guild_id)
                
                for channel in guild.text_channels:
                    y = await channel.create_invite()
                    await ctx.send(y)
                    return
        except:
            embed2 = discord.Embed(title="I'm Not In That Server!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return



def setup(bot):
    bot.add_cog(bulao(bot))