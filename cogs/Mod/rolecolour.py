import discord
import asyncio
from discord.ext import commands
from botprefix import prefix

class rolecolour(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['rc'])
    @commands.has_permissions(manage_roles=True)
    async def rolecolour(self, ctx , role : str = None, col : str = None):


        embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}rolecolor [role] [color]``",colour=0xff0000,timestamp=ctx.message.created_at)

        if not role:
            await ctx.send(embed=embed)
            return

        if not col:
            await ctx.send(embed=embed)
            return

        embed2 = discord.Embed(title="Error: Enter A Valid HEX Code!",colour=0xff0000,timestamp=ctx.message.created_at)

        if col.startswith("#"):
            col = col.replace("#","0X")


        elif col.startswith("0X"):
            pass

        elif col.startswith("0x"):
            pass
                
        else:
            await ctx.send(embed=embed2)
            return

        col2 = col.capitalize()
        try:
            col = int(col,0)
        except:
            await ctx.send(embed=embed2)
            return

        try:
            for rol in ctx.guild.roles:
                if rol.name == role:
                    await rol.edit(reason=None,colour=discord.Colour(col))
                    embed3 = discord.Embed(title=":white_check_mark: Role Colour Changed Successfully!",colour=rol.colour,timestamp=ctx.message.created_at)
                    embed3.add_field(name="Role:",value=f"**{rol.name}**",inline=False)
                    embed3.add_field(name="Color:",value=f"**{col2}**",inline=False)
                    await ctx.send(embed=embed3)
                    return
            
            else:
                embed4 = discord.Embed(title="Error: No Such Role Found!",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed4)
                return
    
        except:
           embed5 = discord.Embed(title="I Don't Have Permissions Or The Role Has Higher Position Than Mine!",colour=0xff0000,timestamp=ctx.message.created_at)
           await ctx.send(embed=embed5)

def setup(bot):
    bot.add_cog(rolecolour(bot))