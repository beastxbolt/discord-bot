import discord
from discord.ext import commands
import asyncio
from asyncio import sleep
from botprefix import prefix

class inrole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(aliases=['ir'])
    async def inrole(self, ctx, *, roleName : str = None):
        
        try:
            if roleName is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}inrole [role_name]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            else:
                i = 0
                for role in ctx.guild.roles:
                    if roleName == "everyone":
                        roleName = "@everyone"
                    if role.name == roleName:
                        l = [m for m in role.members]
                        embed2 = discord.Embed(title=f"⚪ Members In {roleName} Role! ⚪", description="\n".join([f"**{str(m)}**" for m in l]),colour=0x0000ff, timestamp=ctx.message.created_at)
                        for m in role.members:
                            i += 1
                        embed2.set_footer(text=f"Total Members : {i}")


                await ctx.send(embed=embed2)
                return
                

        except:
            embed3 = discord.Embed(title="Role Not Found!",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed3)
            return
        

def setup(bot):
	bot.add_cog(inrole(bot))