import discord
from discord.ext import commands
import asyncio
import time
                        
class pause(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def pause(self,ctx):
        async def pauseFunc():
            ctx.voice_client.pause()
            embed = discord.Embed(title="Paused!",colour=0x0000ff,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return
            
        try:
            if ctx.author.voice is not None:
                if ctx.voice_client is not None:
                    if ctx.author.voice is not None and ctx.author.voice.channel == ctx.voice_client.channel:
                        if ctx.voice_client.is_playing() and ctx.voice_client.is_paused() is False:
                            users = ctx.author.voice.channel.members
                            for member in ctx.author.voice.channel.members:
                                if member.bot:
                                    users.remove(member)
                            if len(users) == 1:
                                await pauseFunc()
                                return
                            else:
                                if ctx.author.guild_permissions.administrator:
                                    await pauseFunc()
                                    return
                                else:
                                    if ctx.author.guild_permissions.manage_channels:
                                        await pauseFunc()
                                        return
                                    else:
                                        for role in ctx.author.roles:
                                            if role.name == "DJ":
                                                await pauseFunc()
                                                return
                                        else:
                                            embed2 = discord.Embed(description="**You Need `Administrator` Permission Or `DJ` Role Or `Manage Channels` Permission To Use This Command!** (Being Alone With The Bot Also Works.)",colour=0xff0000,timestamp=ctx.message.created_at)
                                            await ctx.send(embed=embed2)
                                            return
                        else:
                            embed2 = discord.Embed(title="Player Is Not Playing!",colour=0xff0000,timestamp=ctx.message.created_at)
                            await ctx.send(embed=embed2)
                            return
                    else:
                        embed3 = discord.Embed(title="You Must Be In The Same Voice Channel As The Bot To Use This Command!",colour=0xff0000,timestamp=ctx.message.created_at)
                        await ctx.send(embed=embed3)
                        return
                else:
                    embed4 = discord.Embed(title="I'm Not Connected To A Voice Channel!",colour=0xff0000,timestamp=ctx.message.created_at)
                    await ctx.send(embed=embed4)
                    return
            else:
                embed5 = discord.Embed(title="You Must Be In A Voice Channel To Use This Command!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed5)
                return
        except Exception as e:
            print(e)
            
        

def setup(bot):
    bot.add_cog(pause(bot))