import discord
import asyncio
from discord.ext import commands
import json
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from botprefix import prefix


class google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def google(self,ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}google [search|image] [query]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return


    @google.command()
    async def search(self, ctx, *, query : str = None):

        loading = self.bot.get_emoji(710075331725361272)

        try:
            if query is None:
                embed2 = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}google [search|image] [query]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            else:

                embed3 = discord.Embed(title=f"{loading} Searching...", colour=0x0000ff, timestamp=ctx.message.created_at)
                msg = await ctx.send(embed=embed3)

                cap = DesiredCapabilities().CHROME
                cap["marionette"] = False
                options = Options()
                options.add_argument("--headless")

                driver = webdriver.Chrome(desired_capabilities=cap, chrome_options=options, executable_path=r"C:\chromedriver\chromedriver.exe")
                driver.set_window_size(1366, 768)

                url = f'https://www.google.com/search?rlz=1C1CHBD_enIN909IN909&sxsrf=ALeKk02zSgiPAhyIJJz1h0lV9I8mX8hyGQ:1598794202634&ei=2qlLX9WcJpmY4-EP0IqNiAs&q={query}&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgjECc6BAguEEM6CAguELEDEIMBOggIABCxAxCDAToECAAQQzoKCC4QxwEQowIQQzoFCAAQkQI6BwgAEBQQhwJQpRtYzmZgomloAHAAeACAAeMCiAGoG5IBBzAuNi42LjOYAQCgAQGqAQdnd3Mtd2l6wAEB&sclient=psy-ab&ved=0ahUKEwjV8ZDEhMPrAhUZzDgGHVBFA7EQ4dUDCA0&uact=5'
                driver.get(url)

                driver.set_script_timeout(30)
                driver.set_page_load_timeout(30)

                driver.save_screenshot('./Assets/googlesearch.png')
                driver.quit()

                file = discord.File(fp='./Assets/googlesearch.png', filename='googlesearch.png')
                embed4 = discord.Embed(title=f":mag: Search Results", colour=0x0000ff, timestamp=ctx.message.created_at)
                embed4.set_author(name=ctx.author)
                embed4.set_image(url='attachment://googlesearch.png')
                await msg.delete()
                await ctx.send(file=file, embed=embed4)
                return

        except Exception as e:
            print(e)


    @google.command()
    async def image(self, ctx, *, query : str = None):

        loading = self.bot.get_emoji(710075331725361272)

        try:
            if query is None:
                embed2 = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}google [search|image] [query]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            else:

                embed3 = discord.Embed(title=f"{loading} Searching...", colour=0x0000ff, timestamp=ctx.message.created_at)
                msg = await ctx.send(embed=embed3)

                cap = DesiredCapabilities().CHROME
                cap["marionette"] = False
                options = Options()
                options.add_argument("--headless")

                driver = webdriver.Chrome(desired_capabilities=cap, chrome_options=options, executable_path=r"C:\chromedriver\chromedriver.exe")
                driver.set_window_size(1366, 768)

                url = f'https://www.google.com/search?q={query}&rlz=1C1CHBD_enIN909IN909&sxsrf=ALeKk0185nP25XwPK3-8BsMe7hHpk5OCuQ:1598794399010&source=lnms&tbm=isch&sa=X&ved=2ahUKEwir3uKhhcPrAhU47HMBHVE1CVkQ_AUoAnoECB8QBA&biw=1536&bih=722'
                driver.get(url)

                driver.set_script_timeout(30)
                driver.set_page_load_timeout(30)

                driver.save_screenshot('./Assets/googleimage.png')
                driver.quit()

                file = discord.File(fp='./Assets/googleimage.png', filename='googleimage.png')
                embed4 = discord.Embed(title=f":mag: Search Results", colour=0x0000ff, timestamp=ctx.message.created_at)
                embed4.set_author(name=ctx.author)
                embed4.set_image(url='attachment://googleimage.png')
                await msg.delete()
                await ctx.send(file=file, embed=embed4)


        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(google(bot))