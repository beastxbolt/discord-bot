import discord
from discord.ext import commands
import asyncio
import time
import math
import json
import datetime
import youtube_dl
import sys
import os
import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
from botprefix import prefix
from config import developerKey
import tracemalloc

i = 1

ytdl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
    'usenetrc': True,
    'youtube_include_dash_manifest': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


class play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def search(self, query):
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
            info = ytdl.extract_info(f'ytsearch:{query}', download=False)
            URL = info['entries'][0]['formats'][0]['url']

        yt_id = info['entries'][0]['id']
        yt_url = 'https://www.youtube.com/watch?v=' + yt_id
        title = info['entries'][0]['title']
        time = math.ceil(info['entries'][0]['duration'])
        duration = datetime.timedelta(seconds=time)
        thumbnail = info['entries'][0]['thumbnails'][0]['url']
        channel_name = info['entries'][0]['uploader']
        return {'source': URL, 'title': title, 'duration': duration, 'time': time, 'url': yt_url, 'channelName': channel_name, 'thumbnail': thumbnail, 'ytId': yt_id}


    def urlsearch(self, query):
        with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            URL = info['formats'][0]['url']

        yt_id = info['id']
        yt_url = 'https://www.youtube.com/watch?v=' + yt_id
        title = info['title']
        time = math.ceil(info['duration'])
        duration = datetime.timedelta(seconds=time)
        thumbnail = info['thumbnails'][0]['url']
        channel_name = info['uploader']
        return {'source': URL, 'title': title, 'duration': duration, 'time': time, 'url': yt_url, 'channelName': channel_name, 'thumbnail': thumbnail, 'ytId': yt_id}


    @commands.command(aliases=['p'])
    async def play(self, ctx, *, query: str = None):
        global i

        def after(error):
            try:
                FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                                "options": f"-vn -ss {self.bot.voice_client_attributes[str(ctx.guild.id)]['seek_position']}"}
            except:
                pass
            try:
                try:
                    if self.bot.voice_client_attributes[str(ctx.guild.id)]['seek'] is True:
                        pass
                    else:
                        try:
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop'] is True and self.bot.voice_client_attributes[str(ctx.guild.id)]['loop_queue'] is True:
                                pass
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop'] is True and self.bot.voice_client_attributes[str(ctx.guild.id)]['loop_queue'] is False:
                                pass
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop'] is False and self.bot.voice_client_attributes[str(ctx.guild.id)]['loop_queue'] is False:
                                firstIndex = list(
                                    self.bot.music[str(ctx.guild.id)].keys())[0]
                                self.bot.music[str(ctx.guild.id)].pop(
                                    firstIndex)
                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['loop'] is False and self.bot.voice_client_attributes[str(ctx.guild.id)]['loop_queue'] is True:
                                var = {'move_queue_to_last': True}
                                self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)
                        except:
                            pass
                except:
                    pass

                try:
                    try:
                        if self.bot.voice_client_attributes[str(ctx.guild.id)]['move_queue_to_last'] is True:
                            for key, value in self.bot.music[str(ctx.guild.id)].items():
                                firstIndexKey = key
                                break

                            firstIndex = list(self.bot.music[str(ctx.guild.id)].keys())[0]
                            poppedFirstIndexValue = self.bot.music[str(ctx.guild.id)].pop(firstIndex)
                            self.bot.music[str(ctx.guild.id)][firstIndexKey] = poppedFirstIndexValue

                            checkQueue = list(
                                self.bot.music[str(ctx.guild.id)])[0]
                            requester = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['requester']

                            var = {'move_queue_to_last': False}
                            self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)

                        else:
                            checkQueue = list(
                                self.bot.music[str(ctx.guild.id)])[0]
                            requester = self.bot.music[str(
                                ctx.guild.id)][str(checkQueue)]['requester']
                    

                        if not ctx.voice_client.is_playing():
                            song = self.search(checkQueue)
                            source = song['source']

                            try:
                                findUpcoming = list(
                                    self.bot.music[str(ctx.guild.id)])[1]
                                upcoming = self.bot.music[str(
                                    ctx.guild.id)][str(findUpcoming)]['title']
                            except IndexError:
                                upcoming = "None"
                            
                            ctx.voice_client.play(discord.FFmpegPCMAudio(
                                source=source, **FFMPEG_OPTIONS), after=after)
                            ctx.voice_client.source = discord.PCMVolumeTransformer(
                                ctx.voice_client.source)
                            ctx.voice_client.source.volume = self.bot.voice_client_attributes[str(ctx.guild.id)]['volume'] / 100

                            var = {'seek': False, 'seek_position': '0'}
                            self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)

                            if self.bot.voice_client_attributes[str(ctx.guild.id)]['send_play_embed'] is True:
                                embedx = discord.Embed(
                                    colour=0x32CD32)
                                embedx.add_field(
                                    name="Title", value=f"**[{song['title']}]({song['url']})**", inline=False)
                                embedx.add_field(
                                    name="Channel Name", value=song['channelName'], inline=False)
                                embedx.add_field(
                                    name="Duration", value=song['duration'], inline=False)
                                embedx.add_field(
                                    name="Requested By", value=requester, inline=False)
                                embedx.add_field(
                                    name="Upcoming", value=upcoming, inline=False)
                                embedx.set_thumbnail(
                                    url=song['thumbnail'])
                                embedx.set_author(
                                    name="Started Playing", icon_url="https://media.discordapp.net/attachments/564520348821749766/696332404549222440/4305809_200x130..gif")
                                coroutine = ctx.send(embed=embedx)
                                asyncio.run_coroutine_threadsafe(
                                    coroutine, self.bot.loop)
                            else:
                                var = {'send_play_embed': True}
                                self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)
                        else:
                            return
                    except:
                        pass
                except IndexError:
                    try:
                        time.sleep(120)
                        if ctx.voice_client.is_playing():
                            return
                        else:
                            if ctx.voice_client.is_connected():
                                coroutine2 = ctx.voice_client.disconnect()
                                asyncio.run_coroutine_threadsafe(
                                    coroutine2, self.bot.loop)
                                return
                            else:
                                return
                    except:
                        pass

            except KeyError:
                return

        try:

            if query is None:
                embed = discord.Embed(
                    title=f"This Command Is Used Like This: `{prefix(self.bot, ctx)[0][0]}play [URL/Name]`", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            if ctx.author.voice is not None:
                vc = ctx.author.voice.channel

                if not ctx.voice_client or not ctx.voice_client.is_connected():
                    self.bot.music.pop(str(ctx.guild.id), None)
                    self.bot.voice_client_attributes.pop(str(ctx.guild.id), None)
                    await vc.connect()

                    attr = {"loop": False,
                            "loop_queue": False,
                            "move_queue_to_last": False,
                            "seek": False,
                            "block_skip_and_stop": False,
                            "send_play_embed": True,
                            "seek_position": "0",
                            "volume": 100}

                    value = self.bot.voice_client_attributes.get(str(ctx.guild.id))
                    if value is None:
                        self.bot.voice_client_attributes[str(ctx.guild.id)] = attr
                    else:
                        pass

                    embed2 = discord.Embed(
                        title=f"✅ Connected To `{vc.name}` ✅", colour=0xFF69B4, timestamp=ctx.message.created_at)
                    await ctx.send(embed=embed2)

                if ctx.voice_client.is_connected() and vc != ctx.voice_client.channel:
                    embed3 = discord.Embed(title="You Must Be In The Same Voice Channel As The Bot To Use This Command!",
                                           colour=0xff0000, timestamp=ctx.message.created_at)
                    await ctx.send(embed=embed3)
                    return

                FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                                "options": f"-vn -ss {self.bot.voice_client_attributes[str(ctx.guild.id)]['seek_position']}"}

                try:
                    query = query.strip('<>')

                    try:
                        if "youtube.com/playlist?list=" in query or "youtu.be/playlist?list=" in query or "youtube.com/watch?v=" and "&list=" in query or "youtu.be/" and "&list=" in query:
                            var = {'block_skip_and_stop': True}
                            self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)

                            query = parse_qs(
                                urlparse(query).query, keep_blank_values=True)
                            playlist_id = query["list"][0]

                            youtube = googleapiclient.discovery.build(
                                "youtube", "v3", developerKey=developerKey)

                            request = youtube.playlistItems().list(
                                part="snippet",
                                playlistId=playlist_id,
                                maxResults=100
                            )
                            response = request.execute()
                            playlist_items = []

                            while request is not None:
                                response = request.execute()
                                playlist_items += response["items"]
                                request = youtube.playlistItems().list_next(request, response)

                            msg = await ctx.send(f"0/{len(playlist_items)} Music Added To Queue")
                            for vid in playlist_items:
                                try:
                                    vidIndex = playlist_items.index(vid) + 1
                                    totalIndex = len(playlist_items)
                                    url = f"https://youtube.com/watch?v={vid['snippet']['resourceId']['videoId']}"

                                    song = self.urlsearch(url)
                                    source = song['source']
                                    details = {"title": song['title'],
                                            "url": str(song['url']),
                                            "duration": str(song['duration']),
                                            "time": str(song['time']),
                                            "thumbnail": str(song['thumbnail']),
                                            "requester": str(ctx.author)}

                                    value = self.bot.music.get(str(ctx.guild.id))
                                    if value is None:
                                        self.bot.music[str(ctx.guild.id)] = {}
                                    else:
                                        pass
                                    if str(song['title']) in self.bot.music[str(ctx.guild.id)]:
                                        self.bot.music[str(ctx.guild.id)
                                                    ][str(song['title']) + f" ({i})"] = {}
                                        self.bot.music[str(ctx.guild.id)][str(
                                            song['title']) + f" ({i})"] = details
                                        i += 1
                                    else:
                                        self.bot.music[str(ctx.guild.id)
                                                    ][str(song['title'])] = {}
                                        self.bot.music[str(ctx.guild.id)][str(
                                            song['title'])] = details

                                    try:
                                        findUpcoming = list(
                                            self.bot.music[str(ctx.guild.id)])[1]
                                        upcoming = self.bot.music[str(
                                            ctx.guild.id)][str(findUpcoming)]['title']
                                    except IndexError:
                                        upcoming = "None"

                                    if ctx.voice_client is not None:
                                        if not ctx.voice_client.is_playing():
                                            ctx.voice_client.play(discord.FFmpegPCMAudio(
                                                source=source, **FFMPEG_OPTIONS), after=after)
                                            ctx.voice_client.source = discord.PCMVolumeTransformer(
                                                ctx.voice_client.source)
                                            ctx.voice_client.source.volume = self.bot.voice_client_attributes[str(ctx.guild.id)]['volume'] / 100

                                            embed5 = discord.Embed(colour=0x32CD32)
                                            embed5.add_field(
                                                name="Title", value=f"**[{song['title']}]({song['url']})**", inline=False)
                                            embed5.add_field(
                                                name="Channel Name", value=song['channelName'], inline=False)
                                            embed5.add_field(
                                                name="Duration", value=song['duration'], inline=False)
                                            embed5.add_field(
                                                name="Requested By", value=ctx.author, inline=False)
                                            embed5.add_field(
                                                name="Upcoming", value=upcoming, inline=False)
                                            embed5.set_thumbnail(url=song['thumbnail'])
                                            embed5.set_author(
                                                name="Started Playing", icon_url="https://media.discordapp.net/attachments/564520348821749766/696332404549222440/4305809_200x130..gif")
                                            await ctx.send(embed=embed5)
                                    else:
                                        return
                                    await msg.edit(content=f"{vidIndex}/{totalIndex} Music Added To Queue")
                                except:
                                    continue
                            await msg.edit(content="All Available Music From Playlist Added To Queue!")
                            var = {'block_skip_and_stop': False}
                            self.bot.voice_client_attributes[str(ctx.guild.id)].update(var)

                        else:
                            song = self.search(query)
                            source = song['source']
                            details = {"title": song['title'],
                                    "url": str(song['url']),
                                    "duration": str(song['duration']),
                                    "time": str(song['time']),
                                    "thumbnail": str(song['thumbnail']),
                                    "requester": str(ctx.author)}

                            value = self.bot.music.get(str(ctx.guild.id))
                            if value is None:
                                self.bot.music[str(ctx.guild.id)] = {}
                            else:
                                pass
                            if str(song['title']) in self.bot.music[str(ctx.guild.id)]:
                                self.bot.music[str(ctx.guild.id)
                                            ][str(song['title']) + f" ({i})"] = {}
                                self.bot.music[str(ctx.guild.id)][str(
                                    song['title']) + f" ({i})"] = details
                                i += 1
                            else:
                                self.bot.music[str(ctx.guild.id)
                                            ][str(song['title'])] = {}
                                self.bot.music[str(ctx.guild.id)][str(
                                    song['title'])] = details

                            embed4 = discord.Embed(
                                colour=0xffff00, timestamp=ctx.message.created_at)
                            embed4.add_field(
                                name="Queued", value=f"**[{song['title']}]({song['url']})**", inline=False)
                            embed4.set_author(
                                name="Song Queued", icon_url="https://media.discordapp.net/attachments/564520348821749766/696334217205907516/giphy.gif")
                            await ctx.send(embed=embed4)

                            try:
                                findUpcoming = list(
                                    self.bot.music[str(ctx.guild.id)])[1]
                                upcoming = self.bot.music[str(
                                    ctx.guild.id)][str(findUpcoming)]['title']
                            except IndexError:
                                upcoming = "None"

                            if ctx.voice_client is not None:
                                if not ctx.voice_client.is_playing():
                                    ctx.voice_client.play(discord.FFmpegPCMAudio(
                                        source=source, **FFMPEG_OPTIONS), after=after)
                                    ctx.voice_client.source = discord.PCMVolumeTransformer(
                                        ctx.voice_client.source)
                                    ctx.voice_client.source.volume = self.bot.voice_client_attributes[str(ctx.guild.id)]['volume'] / 100

                                    embed5 = discord.Embed(colour=0x32CD32)
                                    embed5.add_field(
                                        name="Title", value=f"**[{song['title']}]({song['url']})**", inline=False)
                                    embed5.add_field(
                                        name="Channel Name", value=song['channelName'], inline=False)
                                    embed5.add_field(
                                        name="Duration", value=song['duration'], inline=False)
                                    embed5.add_field(
                                        name="Requested By", value=ctx.author, inline=False)
                                    embed5.add_field(
                                        name="Upcoming", value=upcoming, inline=False)
                                    embed5.set_thumbnail(url=song['thumbnail'])
                                    embed5.set_author(
                                        name="Started Playing", icon_url="https://media.discordapp.net/attachments/564520348821749766/696332404549222440/4305809_200x130..gif")
                                    await ctx.send(embed=embed5)
                            else:
                                return

                    except Exception as e:
                        print(e)
                        embed6 = discord.Embed(
                            title=f"No Such Song Found!", colour=0xff0000, timestamp=ctx.message.created_at)
                        await ctx.send(embed=embed6)
                        return

                except Exception as e:
                    print(e)
            else:
                embed7 = discord.Embed(title="You Must Be In A Voice Channel To Use This Command!",
                                       colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed7)
                return
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(play(bot))
