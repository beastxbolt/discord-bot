import discord
from discord.ext import commands
import asyncio
import platform
from botprefix import prefix


class botinfo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command()
	async def botinfo(self, ctx):

		owner = self.bot.get_user(456055164886056961)

		pyv = platform.python_version()
		botos = platform.system()
		discordv = discord.__version__
		e = discord.Embed(description=f"**Bot Information!**", color=0x0ddfff,timestamp=ctx.message.created_at)
		e.add_field(name="• Name", value="8-BIT")
		e.add_field(name="• Prefix", value=prefix(bot, message))
		e.add_field(name="• Owner", value=owner.mention)
		e.add_field(name="• Server Count", value=len(self.bot.guilds))
		e.add_field(name="• Support Server", value="[Click Here](https://discord.com/invite/m4vu7HT)")
		e.add_field(name="• Invite Me", value="[Click Here](https://discord.com/api/oauth2/authorize?client_id=735700750767882300&permissions=8&scope=bot)")
		e.add_field(name="• Python Version", value=pyv)
		e.add_field(name="• OS", value=botos)
		e.add_field(name="• Discord Version", value=discordv)
		await ctx.send(embed=e)



def setup(bot):
	bot.add_cog(botinfo(bot))