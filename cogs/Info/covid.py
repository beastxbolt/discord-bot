import discord
from discord.ext import commands
import asyncio
import requests
from botprefix import prefix


class covid(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def covid(self, ctx,*, countryName=None):
		try:
			if countryName is None:
				embed = discord.Embed(title=f"This Command Is Used Like This:  ``{prefix(self.bot, ctx)[0]}covid [country]``", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=embed)
				return
				
			else:
				url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
				stats = requests.get(url)
				json_stats = stats.json()
				country = json_stats["country"]
				totalCases = json_stats["cases"]
				todayCases = json_stats["todayCases"]
				totalDeaths = json_stats["deaths"]
				todayDeaths = json_stats["todayDeaths"]
				recovered = json_stats["recovered"]
				active = json_stats["active"]
				critical = json_stats["critical"]
				casesPerOneMillion = json_stats["casesPerOneMillion"]
				deathsPerOneMillion = json_stats["deathsPerOneMillion"]
				totalTests = json_stats["totalTests"]
				testsPerOneMillion = json_stats["testsPerOneMillion"]
				
				
				e = discord.Embed(title=f"**COVID-19 Status Of {country}**!",description="This Information Isn't Live Always, Hence It May Not Be Accurate!",colour=0x0000ff,timestamp=ctx.message.created_at)
				e.add_field(name="**Total Cases**",value=totalCases,inline=True)
				e.add_field(name="**Today Cases**",value=todayCases,inline=True)
				e.add_field(name="**Total Deaths**",value=totalDeaths,inline=True)
				e.add_field(name="**Today Deaths**",value=todayDeaths,inline=True)
				e.add_field(name="**Recovered**",value=recovered,inline=True)
				e.add_field(name="**Active**",value=active,inline=True)
				e.add_field(name="**Critical**",value=critical,inline=True)
				e.add_field(name="**Cases Per One Million**",value=casesPerOneMillion,inline=True)
				e.add_field(name="**Deaths Per One Million**",value=deathsPerOneMillion,inline=True)
				e.add_field(name="**Total Tests**",value=totalTests,inline=True)
				e.add_field(name="**Tests Per One Million**",value=testsPerOneMillion,inline=True)
				
				e.set_thumbnail(url="https://cdn.discordapp.com/attachments/564520348821749766/701422183217365052/2Q.png")
				await ctx.send(embed=e)
				
		except:
			ee = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!",colour=0xff0000,timestamp=ctx.message.created_at)
			ee.set_author(name="Error!")
			await ctx.send(embed=ee)



def setup(bot):
	bot.add_cog(covid(bot))