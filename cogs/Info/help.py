import discord
from discord.ext import commands
import asyncio
from asyncio import TimeoutError
import json
from botprefix import prefix



class help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.bot.remove_command('help')
		
	
	@commands.command()
	async def help(self, ctx):

		moneybag_emoji = '\U0001F4B0' #economy
		fun_emoji = '\U0001F9F0' #fun
		gambling_emoji = '\U0001F3AE' #game
		mod_emoji = '\U0001F6E0' #mod
		owneronly_emoji = '\U0001F451' #owner
		info_emoji = '\U0001F50E' #info
		utility_emoji = '\U0001F579' #utility
		music_emoji = '\U0001F3B5' #music
		cross_emoji = '\U0000274C' #cross
		home_emoji = '\U0001F3E0' #home
		next_emoji = '\U000023ED' #next
		previous_emoji = '\U000023EE' #previous
		
		embed = discord.Embed(title="➡️  Help Commands ``Page 1``  ⬅️",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed.add_field(name="💰 Economy Commands 💰",value="**Economy Related Commands!**",inline=False)
		embed.add_field(name="🧰 Fun Commands 🧰",value="**Interact With Fun Commands!**",inline=False)
		embed.add_field(name="🎮 Gambling Commands 🎮",value="**Gambling Related Commands!**",inline=False)
		embed.add_field(name="🛠️ Moderation Commands 🛠️",value="**Moderation Commands For Bot Like Kick, Ban, Mute etc!**",inline=False)
		embed.add_field(name="👑 Owner-Only Commands 👑",value="**Only Bot Owner(s) Can Use These Commands!**",inline=False)
		embed.add_field(name="🔎 Information Commands 🔎",value="**Information & Search Commands!**",inline=False)
		embed.add_field(name="⏭️ Next Page ⏭️",value="**Opens Next Page Of The Menu!**",inline=False)
		embed.add_field(name="❌ Close Menu ❌",value="**Closes The Help Menu!**",inline=False)
		



		embed1 = discord.Embed(title="➡️  Help Commands ``Page 2``  ⬅️",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed1.add_field(name="🕹️ Utility Commands 🕹️",value="**Utility Commands For The Bot!**",inline=False)
		embed1.add_field(name="🎵 Music Commands 🎵",value="**Music Related Commands!**",inline=False)
		embed1.add_field(name="⏮️ Previous Page ⏮️",value="**Opens Previous Page Of The Menu!**",inline=False)
		embed1.add_field(name="❌ Close Menu ❌",value="**Closes The Help Menu!**",inline=False)

		
		
		msg = await ctx.send(embed=embed)
		await msg.add_reaction(emoji = moneybag_emoji)
		await msg.add_reaction(emoji = fun_emoji)
		await msg.add_reaction(emoji = gambling_emoji)
		await msg.add_reaction(emoji = mod_emoji)
		await msg.add_reaction(emoji = owneronly_emoji)
		await msg.add_reaction(emoji = info_emoji)
		await msg.add_reaction(emoji = next_emoji)
		await msg.add_reaction(emoji = cross_emoji)
		

		embed2 = discord.Embed(title="💰 Economy Commands 💰",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}balance",value="View Gems Aavailable In Your Wallet!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}bank",value="View Gems Aavailable In Your Bank!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}beg",value="Get Gems From People & A Chance To Get An Item!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}buy [item]",value="Buy An Item From The Shop!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}daily",value="Collect Gems After Every 24 Hours!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}deposit [amount]",value="Deposit Gems To Your Bank!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}give [user] [amount]",value="Give Your Gems To Another User!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}leaderboard",value="Shows Global Economy Leaderboard!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}postmeme",value="Post Sweet Memes For Ad Revenues!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}profile",value="View Your Profile Card!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}register",value="Register Yourself On The Database!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}sell [item]",value="Sell An Item You Own!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}shop",value="Open Shop & View Items Available To Purchase!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}transactions",value="Shows Last 10 Recent Transactions!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}use [item]",value="Use An Item You Own!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}withdraw [amount]",value="Withdraw Gems From Your Bank!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}xp",value="Shows Your XP Info!",inline=False)
		embed2.add_field(name=f"{prefix(self.bot, ctx)[0]}xpleaderboard",value="Shows XP Leaderboard Of The Server!",inline=False)

		




		embed3 = discord.Embed(title="🧰 Fun Commands 🧰",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}askdan [question]",value="Get Your Questions Answered By Dan!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}big [text]",value="Replaces Text With Emojis!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}bigtext [text]",value="Replaces Text With Big Font!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}choose [choice1] [choice2]",value="Bot Chooses From Two Options!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}insult [user]",value="Insults A User!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}joke",value="Get A Random Joke!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}meme",value="Get A Random Meme!",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}rip [user]",value="Sends A RIP Image Of A User",inline=False)
		embed3.add_field(name=f"{prefix(self.bot, ctx)[0]}slap [user] [reason]",value="Slaps A User For The Given Reason!",inline=False)




		embed4 = discord.Embed(title="🎮 Gambling Commands 🎮",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed4.add_field(name=f"{prefix(self.bot, ctx)[0]}coinflip [h|t] [bet amount]",value="Flip Coins And Earn Gems!",inline=False)
		embed4.add_field(name=f"{prefix(self.bot, ctx)[0]}guess [bet]",value="Guess Numbers And Earn Gems!",inline=False)
		embed4.add_field(name=f"{prefix(self.bot, ctx)[0]}rolldice [number1] [number2] [bet amount]",value="Roll Dice And Earn Gems!",inline=False)
		embed4.add_field(name=f"{prefix(self.bot, ctx)[0]}rps [r|p|s] [bet amount]",value="Play Rock, Paper & Scissor And Earn Gmes!",inline=False)



		
		
		embed5 = discord.Embed(title="🛠️ Moderation Commands 🛠️",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}ban [user] [reason]",value="Bans A User From The Server!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}clear [number of messages]",value="Deletes The Given Number Of Messages!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}disable",value="Disables A Command Or System!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}dm [user]",value="DM A User Through The Bot!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}enable",value="Enables A Command Or System!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}giverole [user] [rolname]",value="Gives A Role To The User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}kick [user] [reason]",value="Kicks A User From The Server!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}lockchannel [channel(optional)]",value="Locks A Channel For @everyone Role!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}mute [user] [reason]",value="Mutes A User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}nick [user] [new nickname]",value="Changes The Nickname Of A User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}rolecolour [rolename] [colour hex]",value="Changes The Colour Of A Role!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}slowmode [time(in sec)]",value="Sets Slowmode In The Channel!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}takerole [user] [rolename]",value="Removes Role From A User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}tempmute [user] [time(in min)] [reason]",value="Temporarily Mutes A User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}unban [user]",value="Unbans A User From The Server!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}unlockchannel [channel(optional)]",value="Unlocks A Channel For @everyone Role!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}unmute [user]",value="Unmutes A User!",inline=False)
		embed5.add_field(name=f"{prefix(self.bot, ctx)[0]}warn [user] [reason]",value="Warns A User!",inline=False)




		embed6 = discord.Embed(title="👑 Owner-Only Commands 👑",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}eval [code]",value="Evaluates A Given Code!",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}gift [user] [gems]",value="Sends Gift To A User!",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}load [module]",value="Loads A Module!",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}reload [module]",value="Reloads A Module!",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}restart",value="Restarts The Bot",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}shutdown",value="Shuts Down The Bot!",inline=False)
		embed6.add_field(name=f"{prefix(self.bot, ctx)[0]}unload [module]",value="Unloads A Module!",inline=False)




		embed7 = discord.Embed(title="🔎 Information Commands 🔎",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}avatar [user]",value="Shows A User's Avatar!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}botinfo",value="Shows Bot's Info!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}covid [country]",value="Shows A Country's COVID Info!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}emoji [emoji]",value="Shows An Emoji's Info!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}help",value="Shows This Help Message!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}humans",value="Shows The Number Of Humans In The Server!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}inrole [role name]",value="Shows The Users In A Role!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}members",value="Shows The Number Of Members In The Server!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}ping",value="Shows The Bot's Latency!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}serverinfo",value="Shows Server Info!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}uptime",value="Shows Bot's Uptime!",inline=False)
		embed7.add_field(name=f"{prefix(self.bot, ctx)[0]}userinfo [user]",value="Shows A User's Info!",inline=False)
		
		
		
		
		embed8 = discord.Embed(title="🕹️ Utility Commands 🕹️",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}alarm [time(in min)] [reminder]",value="Sets Alarm With Reminder!",inline=False)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}invite",value="Get Invite Link Of The Bot!",inline=False)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}say [message]",value="Send Message Through The Bot In The Channel!",inline=False)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}roles",value="Get All The Roles Of The Server!",inline=False)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}set [levelup|suggestion]",value="Sets Levelup And Suggestion Channel!",inline=False)
		embed8.add_field(name=f"{prefix(self.bot, ctx)[0]}suggest [suggestion]",value="Post A Suggestion!**",inline=False)
		
		



		embed9 = discord.Embed(title="🎵 Music Commands 🎵",colour=0xff00ff,timestamp=ctx.message.created_at)
		embed9.add_field(name=f"{prefix(self.bot, ctx)[0]}join",value="Connects The Bot To A Voice Channel!",inline=False)
		embed9.add_field(name=f"{prefix(self.bot, ctx)[0]}disconnect",value="Disconnects The Bot From A Voice Channel!",inline=False)



		embed10 = discord.Embed(title="Help Message Has Been Has Been Closed!",colour=0xff0000,timestamp=ctx.message.created_at)

		
		
		def check(reaction, user):
			return not user.bot and user.id == ctx.author.id
			
		try:
			while True:
				reaction, user = await self.bot.wait_for('reaction_add', timeout=120.0, check=check)
				
				if reaction.emoji == moneybag_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed2)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)
					
				elif reaction.emoji == fun_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed3)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)

					
				elif reaction.emoji == gambling_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed4)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)
					
				elif reaction.emoji == mod_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed5)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)
					
				elif reaction.emoji == owneronly_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed6)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)

				elif reaction.emoji == info_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed7)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)

				elif reaction.emoji == utility_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed8)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)

				elif reaction.emoji == music_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed9)
					await msg.add_reaction(emoji = home_emoji)
					await msg.add_reaction(emoji = cross_emoji)


				elif reaction.emoji == cross_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed10)
					return

				elif reaction.emoji == home_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed)
					await msg.add_reaction(emoji = moneybag_emoji)
					await msg.add_reaction(emoji = fun_emoji)
					await msg.add_reaction(emoji = gambling_emoji)
					await msg.add_reaction(emoji = mod_emoji)
					await msg.add_reaction(emoji = owneronly_emoji)
					await msg.add_reaction(emoji = info_emoji)
					await msg.add_reaction(emoji = next_emoji)
					await msg.add_reaction(emoji = cross_emoji)

				elif reaction.emoji == next_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed1)
					await msg.add_reaction(emoji = utility_emoji)
					await msg.add_reaction(emoji = music_emoji)
					await msg.add_reaction(emoji = previous_emoji)
					await msg.add_reaction(emoji = cross_emoji)


				elif reaction.emoji == previous_emoji:
					await msg.clear_reactions()
					await msg.edit(embed=embed)
					await msg.add_reaction(emoji = moneybag_emoji)
					await msg.add_reaction(emoji = fun_emoji)
					await msg.add_reaction(emoji = gambling_emoji)
					await msg.add_reaction(emoji = mod_emoji)
					await msg.add_reaction(emoji = owneronly_emoji)
					await msg.add_reaction(emoji = info_emoji)
					await msg.add_reaction(emoji = next_emoji)
					await msg.add_reaction(emoji = cross_emoji)

				
		except asyncio.TimeoutError:
			await msg.clear_reactions()
			return


def setup(bot):
	bot.add_cog(help(bot))