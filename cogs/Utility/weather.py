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
import json
from botprefix import prefix


class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def weather(self, ctx, place : str = None):

        if place is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}weather [place]``",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)

        else:
            try:
                url = f"https://weather.ls.hereapi.com/weather/1.0/report.json?product=forecast_hourly&name={place}&apiKey=zgzVmU4HPct2yx7wVYa-XEKGRw6pyiRHmFuT1jbgpZk"
                
                info = requests.get(url)
                json_info = info.json()
                sky_desc = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['description']
                temp = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['temperature']
                humidity = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['humidity']
                windspeed = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['windSpeed']
                winddirec = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['windDesc']
                visibility = json_info['hourlyForecasts']['forecastLocation']['forecast'][0]['visibility']

                embed2 = discord.Embed(title="⛅Weather⛅",description=f"**Hourly Weather of {place.upper()}!**",color=0x0000ff,timestamp=ctx.message.created_at)
                embed2.add_field(name="☁️ Sky Description",value=f"**{sky_desc}**",inline=False)
                embed2.add_field(name="🌡️ Temperature",value=f"**{temp} °C**",inline=False)
                embed2.add_field(name="💦 Humidity",value=f"**{humidity}**",inline=False)
                embed2.add_field(name="🌬️ Wind Speed",value=f"**{windspeed}**",inline=False)
                embed2.add_field(name="💨 Wind Direction",value=f"**{winddirec}**",inline=False)
                embed2.add_field(name="🌫️ Visibility",value=f"**{visibility}**",inline=False)
                embed2.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed2.set_thumbnail(url=self.bot.user.avatar_url)
                await ctx.send(embed=embed2)

            except:
                embed3 = discord.Embed(title="Invalid Location!",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)



def setup(bot):
	bot.add_cog(weather(bot))