import discord
from discord.ext import commands
import asyncio
import datetime


class queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['q'])
    async def queue(self, ctx, page=1):
        if not isinstance(page, int):
            embed = discord.Embed(title="Enter A Valid Number!",
                                  colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        if page <= 0:
            embed2 = discord.Embed(
                title="Enter A Valid Number!", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return

        try:
            if ctx.author.voice is not None:
                if ctx.voice_client is not None:
                    if ctx.author.voice is not None and ctx.author.voice.channel == ctx.voice_client.channel:
                        if ctx.voice_client.is_playing():
                            list_collection = []
                            checkQueue = list(
                                self.bot.music[str(ctx.guild.id)])[0]
                            title = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['title']
                            url = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['url']
                            duration = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['duration']
                            requester = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['requester']

                            complete_list = ""
                            complete_list = complete_list + "**__Now Playing:__**\n" + f"[{title}]({url})" + " | " + f" `{duration} Requested By: {requester}`" + "\n\n**__Up Next:__**\n"
                            musicList = list(self.bot.music[str(ctx.guild.id)])
                            i = 0
                            skipFirst = 0
                            for music in musicList:
                                if skipFirst == 0:
                                    skipFirst += 1
                                else:
                                    title = self.bot.music[str(
                                        ctx.guild.id)][str(music)]['title']
                                    url = self.bot.music[str(
                                        ctx.guild.id)][str(music)]['url']
                                    duration = self.bot.music[str(
                                        ctx.guild.id)][str(music)]['duration']
                                    requester = self.bot.music[str(
                                        ctx.guild.id)][str(music)]['requester']

                                    complete_list = complete_list + f"`{i + 1}.` [{title}]({url})" + " | " + f" `{duration} Requested By: {requester}`" + "\n\n"
                                    i = i + 1
                                    if i % 10 == 0:
                                        list_collection.append(complete_list)
                                        complete_list = ''

                            if i % 10 != 0 or i == 0:
                                list_collection.append(complete_list)

                            selection = page - 1
                            embed3 = discord.Embed(
                                title=f"Queue For {ctx.guild.name}", color=0xadd8e6)
                            loopStatus = ""
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop'] is True:
                                loopStatus = loopStatus + "✅"
                            else:
                                loopStatus = loopStatus + "❌"

                            loopqueueStatus = ""
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop_queue'] is True:
                                loopqueueStatus = loopqueueStatus + "✅"
                            else:
                                loopqueueStatus = loopqueueStatus + "❌"                            

                            text = ""
                            if i <= 1:
                                text += "music"
                            if i > 1:
                                text += "musics"

                            totalMusicLengthInInteger = 0
                            skipFirstIndex = 0
                            for key, value in self.bot.music[str(ctx.guild.id)].items():
                                if skipFirstIndex == 0:
                                    skipFirstIndex += 1
                                else:
                                    totalMusicLengthInInteger += int(value['time'])
                            lengthInString =  datetime.timedelta(seconds=totalMusicLengthInInteger)
                            totalMusicLength = f"{lengthInString} total length"

                            if int(selection) < 0:
                                list_collection[0] += f"**{i} {text} in queue | {totalMusicLength}**"
                                embed3.description = list_collection[0]
                                embed3.set_footer(text="Page: 1/" + str(len(list_collection)) +
                                                f" | Loop: {loopStatus} | Loop Queue: {loopqueueStatus}", icon_url=ctx.author.avatar_url)
                            elif int(selection) > len(list_collection) - 1:
                                list_collection[len(list_collection) -
                                                1] += f"**{i} {text} in queue | {totalMusicLength}**"
                                embed3.description = list_collection[len(
                                    list_collection) - 1]
                                embed3.set_footer(text="Page: " + str(len(list_collection)) + "/" + str(
                                    len(list_collection)) + f" | Loop: {loopStatus} | Loop Queue: {loopqueueStatus}", icon_url=ctx.author.avatar_url)
                            else:
                                list_collection[selection] += f"**{i} {text} in queue | {totalMusicLength}**"
                                embed3.description = list_collection[selection]
                                embed3.set_footer(text="Page: " + str(page) + "/" + str(
                                    len(list_collection)) + f" | Loop: {loopStatus} | Loop Queue: {loopqueueStatus}", icon_url=ctx.author.avatar_url)
                            await ctx.send(embed=embed3)
                            return
                        else:
                            embed4 = discord.Embed(
                                title=f"Queue For {ctx.guild.name}", description="Nothing is playing, let's get this party started! :tada:", color=0xadd8e6)
                            await ctx.send(embed=embed4)
                            return
                    else:
                        embed5 = discord.Embed(title="You Must Be In The Same Voice Channel As The Bot To Use This Command!",colour=0xff0000,timestamp=ctx.message.created_at)
                        await ctx.send(embed=embed5)
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
    bot.add_cog(queue(bot))
