import discord
import discord
from discord.ext import commands
import asyncio
import random
import requests
import json
from botprefix import prefix

class animesearch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def animesearch(self, ctx, name : str = None):
        try:

            if name is None:
                embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}animesearch [name]``", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return
            
            else:
                url = f"https://api.jikan.moe/v3/search/anime?q={name}"
                anime = requests.get(url)
                json_anime = anime.json()
                anime_url = json_anime["results"][0]["url"]
                image_url = json_anime["results"][0]["image_url"]
                anime_title = json_anime["results"][0]["title"]
                airing = json_anime["results"][0]["airing"]
                summary = json_anime["results"][0]["synopsis"]
                sub_type = json_anime["results"][0]["type"]
                episodes = json_anime["results"][0]["episodes"]
                score = json_anime["results"][0]["score"]
                start_date = json_anime["results"][0]["start_date"]
                end_date = json_anime["results"][0]["end_date"]
                rating = json_anime["results"][0]["rated"]


                embed2 = discord.Embed(title=f"**{anime_title}**", url=anime_url, description=summary ,colour = 0x00ffff,timestamp=ctx.message.created_at)
                embed2.add_field(name=":date: Aired Date:", value=f"**{start_date} To {end_date}**", inline=False)
                embed2.add_field(name=":hourglass_flowing_sand: Airing:", value=f"**{airing}**", inline=False)
                embed2.add_field(name=":file_folder: Sub-Type:", value=f"**{sub_type}**", inline=False)
                embed2.add_field(name=":cd: Episode Count:", value=f"**{episodes}**", inline=False)
                embed2.add_field(name=":bar_chart: Score:", value=f"**{score}**", inline=False)
                embed2.add_field(name=":star: Rating", value=f"**{rating}**", inline=False)
                embed2.set_thumbnail(url=image_url)
                embed2.set_author(name=ctx.author)

                await ctx.send(embed=embed2)
                return
            
        except:
            embed3 = discord.Embed(title="Invalid Anime Name Or API Error! Try Again..!",colour=0xff0000,timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)


def setup(bot):
	bot.add_cog(animesearch(bot))