import discord
import asyncio
from discord.ext import commands
import json
import googletrans
from googletrans import Translator
from botprefix import prefix


class translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['googletranslate', 'googletrans', 'trans'])
    async def translate(self, ctx, lang : str = None, *, text : str = None):

        translator = Translator()

        if lang is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}translate [langauge] [text]``",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        if text is None:
            embed2 = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}translate [langauge] [text]``",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed2)
            return

        else:
            try:
                result = translator.translate(text, dest=lang)
                embed3 = discord.Embed(title="Translation", colour=0xcc00ff, timestamp=ctx.message.created_at)
                embed3.add_field(name="**From**", value=result.src.upper(), inline=False)
                embed3.add_field(name="**To**", value=result.dest.upper(), inline=False)
                embed3.add_field(name="**Translation**", value=result.text, inline=False)
                embed3.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed3.set_thumbnail(url=self.bot.user.avatar_url)
                await ctx.send(embed=embed3)
                return

            except:
                embed4 = discord.Embed(title=f"The Language '{lang}' Is Not Supported!",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed4)
                return



def setup(bot):
	bot.add_cog(translate(bot))