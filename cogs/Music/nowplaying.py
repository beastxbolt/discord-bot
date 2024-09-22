import discord
from discord.ext import commands
import asyncio
import youtube_dl
import datetime


class nowplaying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['np'])
    async def nowplaying(self, ctx):
        try:
            if ctx.author.voice is not None:
                if ctx.voice_client is not None:
                    if ctx.author.voice is not None and ctx.author.voice.channel == ctx.voice_client.channel:
                        if ctx.voice_client.is_playing() or ctx.voice_client.is_playing() is False and ctx.voice_client.is_paused() is True:
                            try:
                                checkQueue = list(
                                    self.bot.music[str(ctx.guild.id)])[0]
                                title = self.bot.music[str(
                                    ctx.guild.id)][str(checkQueue)]['title']
                                url = self.bot.music[str(
                                    ctx.guild.id)][str(checkQueue)]['url']
                                requester = self.bot.music[str(
                                    ctx.guild.id)][str(checkQueue)]['requester']
                                thumbnail = self.bot.music[str(
                                    ctx.guild.id)][str(checkQueue)]['thumbnail']
                                duration = self.bot.music[str(
                                    ctx.guild.id)][str(checkQueue)]['duration']

                                embed = discord.Embed(colour=0x0067ff)
                                embed.set_author(name="Now Playing ♪")
                                embed.set_thumbnail(url=thumbnail)
                                embed.description = f"**[{title}]({url})**\n\n" + f"`Requested By:` {requester}\n" + f"`Duration:` {duration}"
                                await ctx.send(embed=embed)
                                return
                            except Exception as e:
                                print(e)

                        else:
                            embed2 = discord.Embed(
                                title="Player Is Not Playing!", colour=0xff0000, timestamp=ctx.message.created_at)
                            await ctx.send(embed=embed2)
                            return
                    else:
                        embed3 = discord.Embed(
                            title="You Must Be In The Same Voice Channel As The Bot To Use This Command!", colour=0xff0000, timestamp=ctx.message.created_at)
                        await ctx.send(embed=embed3)
                        return
                else:
                    embed4 = discord.Embed(
                        title="I'm Not Connected To A Voice Channel!", colour=0xff0000, timestamp=ctx.message.created_at)
                    await ctx.send(embed=embed4)
                    return
            else:
                embed5 = discord.Embed(title="You Must Be In A Voice Channel To Use This Command!",
                                       colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed5)
                return
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(nowplaying(bot))
