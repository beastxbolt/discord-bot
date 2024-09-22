import discord
import asyncio
from discord.ext import commands
import sqlite3
from sqlite3 import connect
import datetime
from botprefix import prefix

db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()



class claim(commands.Cog):
	def __init__(self,bot):
		self.bot = bot


	@commands.command()
	async def claim(self,ctx, code : int = None):

		tada = self.bot.get_emoji(709752857653673994)
		gem = self.bot.get_emoji(710105510984286238)

		try:
		
			if code is None:
				embed = discord.Embed(title=f"This Command Is Used Like This: ```{prefix(self.bot, ctx)[0]}claim [giftcode]```",colour=0xff0000,timestamp=ctx.message.created_at)
				await ctx.send(embed=embed)
				return

			giftcodeCheck = cursor.execute(f"SELECT code FROM giftcode WHERE code = {code}").fetchone()
			
			if giftcodeCheck is None:
				embed2 = discord.Embed(title="The Giftcode Is Either Invalid Or Has Been Already Claimed!", colour=0xff0000, timestamp=ctx.message.created_at)
				await ctx.send(embed=embed2)
				return

			else:
				await asyncio.sleep(0.5)
				giftValue = cursor.execute(f"SELECT value FROM giftcode WHERE code = {code}").fetchone()
				embed3 = discord.Embed(title=f"You Have Claimed A Giftcode! {tada}", colour=0x00ff00, timestamp=ctx.message.created_at)
				embed3.add_field(name="• Code", value=code)
				embed3.add_field(name="• Value", value=f"{giftValue[0]} {gem}")
				embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
				await ctx.send(embed=embed3)

				cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (giftValue[0], ctx.author.id))
				db.commit()

				cursor.execute(f"DELETE FROM giftcode WHERE code = {code}")
				db.commit()

				time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
				cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Claimed A Giftcode!", "+" + f"{giftValue[0]}", time, ctx.author.id))
				db.commit()
				return
		except Exception as e:
			print(e)



def setup(bot):
	bot.add_cog(claim(bot))