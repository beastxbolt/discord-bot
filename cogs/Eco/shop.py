import discord
import asyncio
import os
import datetime
import math
import requests
import random
from random import choice, randrange
from asyncio import sleep
from discord.ext import commands
from asyncio import TimeoutError
import sqlite3
from sqlite3 import connect
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import urllib.request


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class shop(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def shop(self,ctx):
        
            gem = self.bot.get_emoji(710105510984286238)
            tada = self.bot.get_emoji(709752857653673994)
            loading = self.bot.get_emoji(710075331725361272)
        
        
            bag = '\U0001F6CD'
            money = '\U0001F4B0'
            cross = '\U0000274C'
            home_emoji = '\U0001F3E0'
            
            ee = discord.Embed(title="🛒 **SHOP** 🛒",description="**What Do You Want To Buy Today?**",color=0xff00ff,timestamp=ctx.message.created_at)
            ee.add_field(name="🛍️ Item Shop🛍️",value="**React With 🛍️ To View Items!**",inline=False)
            ee.add_field(name="💰 Premium Shop 💰",value="**React With 💰 To View Premium Items!**",inline=False)
            ee.add_field(name="❌ Exit Shop ❌",value="**I Don't Want To Buy Anything!**",inline=False)
            
            
            msg = await ctx.send(embed=ee)
            await msg.add_reaction(emoji = bag)
            await msg.add_reaction(emoji = money)
            await msg.add_reaction(emoji = cross)
            
            
            item = discord.Embed(title="🛍️ Item Shop 🛍️",color=0xff00ff,timestamp=ctx.message.created_at)
            item.add_field(name=f"**`#1` :card_index: Premium Membership :card_index: **",value=f"**Price: 20000 {gem}\nGives You Premium Membership And Access To Premium Features!\nTo Buy Send `++buy premium`**",inline=False)
            item.add_field(name=f"**`#2` :ballot_box: Loot Box :ballot_box: **",value=f"**Price: 1000 {gem}\nGives Random Amount Of Gems Between 200 and 2000!\nTo Buy Send `++buy lootbox`**",inline=False)
            
            
            
            prem = discord.Embed(title="💰 Premium Shop 💰",colour=0xff00ff,timestamp=ctx.message.created_at)
            prem.add_field(name=f"**:crystal_ball: Premium Meme Command :crystal_ball: **",value=f"**Price: 4000 {gem}\nGives Access To Premium Meme Command!\nTo Buy Send `++buy meme`**",inline=False)
            prem.add_field(name=f"**:round_pushpin:Premium Insult Command:round_pushpin:**",value=f"**Price: 8000 {gem}\nGives Access To Premium Insult Command!\nTo Buy Send `++buy insult`**",inline=False)
            
            
            close = discord.Embed(title="Shop Has Been Closed By The User!",color=0xff00ff,timestamp=ctx.message.created_at)
                    
            
            def check(reaction, user):
                return not user.bot and user.id == ctx.author.id
                
            try:
                while True:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=120, check=check)
                    
                    if reaction.emoji == bag:
                        await msg.clear_reactions()
                        await msg.edit(embed=item)
                        await msg.add_reaction(emoji = home_emoji)
                        await msg.add_reaction(emoji = cross)
                        
                    elif reaction.emoji == money:
                        await msg.clear_reactions()
                        await msg.edit(embed=prem)
                        await msg.add_reaction(emoji = home_emoji)
                        await msg.add_reaction(emoji = cross)

                    elif reaction.emoji == home_emoji:
                        await msg.clear_reactions()
                        await msg.edit(embed=ee)
                        await msg.add_reaction(emoji = bag)
                        await msg.add_reaction(emoji = money)
                        await msg.add_reaction(emoji = cross)
                        
                    elif reaction.emoji == cross:
                        await msg.clear_reactions()
                        await msg.edit(embed=close)
                        return
                    
            except asyncio.TimeoutError:
                await msg.clear_reactions()
                return



def setup(bot):
	bot.add_cog(shop(bot))