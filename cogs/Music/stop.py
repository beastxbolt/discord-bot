import discord
from discord.ext import commands
import asyncio
import time

class stop(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def stop(self, ctx):

        async def stopFunc():
            self.bot.music.pop(str(ctx.guild.id), None)
            ctx.voice_client.stop()
            embed = discord.Embed(title="Stopped!",colour=0x0000ff,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        try:
            if ctx.author.voice is not None:
                if ctx.voice_client is not None:
                    if ctx.author.voice is not None and ctx.author.voice.channel == ctx.voice_client.channel:
                        if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['block_skip_and_stop'] is False:
                                users = ctx.author.voice.channel.members
                                for member in ctx.author.voice.channel.members:
                                    if member.bot:
                                        users.remove(member)
                                if len(users) == 1:
                                    await stopFunc()
                                    return
                                else:
                                    if ctx.author.guild_permissions.administrator:
                                        await stopFunc()
                                        return
                                    else:
                                        if ctx.author.guild_permissions.manage_channels:
                                            await stopFunc()
                                            return
                                        else:
                                            for role in ctx.author.roles:
                                                if role.name == "DJ":
                                                    await stopFunc()
                                                    return
                                            else:
                                                embed2 = discord.Embed(description="**You Need `Administrator` Permission Or `DJ` Role Or `Manage Channels` Permission To Use This Command!** (Being Alone With The Bot Also Works.)",colour=0xff0000,timestamp=ctx.message.created_at)
                                                await ctx.send(embed=embed2)
                                                return
                            else:
                                embed3 = discord.Embed(title="Cannot Stop While Adding Playlist In Queue!",colour=0xff0000,timestamp=ctx.message.created_at)
                                await ctx.send(embed=embed3)
                                return
                        else:
                            embed4 = discord.Embed(title="Player Is Not Playing!",colour=0xff0000,timestamp=ctx.message.created_at)
                            await ctx.send(embed=embed4)
                            return
                    else:
                        embed5 = discord.Embed(title="You Must Be In The Same Voice Channel As The Bot To Use This Command!",colour=0xff0000,timestamp=ctx.message.created_at)
                        await ctx.send(embed=embe5)
                        return
                else:
                    embed6 = discord.Embed(title="I'm Not Connected To A Voice Channel!",colour=0xff0000,timestamp=ctx.message.created_at)
                    await ctx.send(embed=embed6)
                    return
            else:
                embed7 = discord.Embed(title="You Must Be In A Voice Channel To Use This Command!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed7)
                return
        except Exception as e:
            print(e)
        
def setup(bot):
    bot.add_cog(stop(bot))