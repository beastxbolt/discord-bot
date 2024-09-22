import discord
import asyncio
from discord.ext import commands
import random
from botprefix import prefix


class standoff(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def standoff(self, ctx, member : discord.Member = None):

        try:

            revolver_right = self.bot.get_emoji(804933100106678302)
            revolver_left = self.bot.get_emoji(804930875153186870)
            tumbleweed = self.bot.get_emoji(804936357993906229)
            pensive_cowboy = self.bot.get_emoji(805067715575939093)
            time = random.randrange(3, 6)
            emoji = random.choice(['💥', tumbleweed, '💥', tumbleweed])

            if member is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}standoff [user]``",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return
            
            else:
                embed2 = discord.Embed(description=f":bangbang: **{ctx.author.name}** and **{member.name}** are having a standoff.\nThe first person to click the :boom: when it appears will win.")
                msg = await ctx.send(f":cowboy:{revolver_right}          {revolver_left}:cowboy:", embed=embed2)

                await asyncio.sleep(time)
                await msg.add_reaction(emoji = emoji)

                if emoji == tumbleweed:
                        await msg.add_reaction(emoji = '💥')
                else:
                    pass 

                def check(reaction, user):
                    return not user.bot and user == ctx.author or user == member
                    
                try:
                    while True:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)
                            
                        if reaction.emoji == "💥" and user == ctx.author and ctx.author.bot == False:
                            embed3 = discord.Embed(description=f"**{ctx.author.name}** won!")
                            await msg.edit(content=f":cowboy:{revolver_right}          {revolver_left}:boom:", embed=embed3)
                            return

                        elif reaction.emoji == "💥" and user == member and member.bot == False:
                            embed4 = discord.Embed(description=f"**{member.name}** won!")
                            await msg.edit(content=f":boom:{revolver_right}          {revolver_left}:cowboy:", embed=embed4)
                            return

                        elif reaction.emoji == tumbleweed and user == ctx.author and ctx.author.bot == False:
                            embed5 = discord.Embed(description=f"**{ctx.author.name}** shot too early!")
                            await msg.edit(content=f"{pensive_cowboy}{revolver_right}          {revolver_left}:boom:", embed=embed5)
                            return

                        elif reaction.emoji == tumbleweed and user == member and member.bot == False:
                            embed6 = discord.Embed(description=f"**{member.name}** shot too early!")
                            await msg.edit(content=f":boom:{revolver_right}          {revolver_left}{pensive_cowboy}", embed=embed6)
                            return    

                except asyncio.TimeoutError:
                    await msg.edit("No One Responded, The Match Is Over!")
                    return

        except Exception as e:
            print(e)
                        



def setup(bot):
	bot.add_cog(standoff(bot))