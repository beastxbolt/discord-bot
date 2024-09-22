import discord
import asyncio
from discord.ext import commands
from botprefix import prefix


class lockchannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['lc'])
    @commands.has_permissions(manage_channels = True)
    async def lockchannel(self, ctx, channel : discord.TextChannel = None, *, roleName : str = None):

        try:

            if channel is None:
                embed = discord.Embed(description=f"**This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}lockchannel [channel] [role name]``**",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            if roleName is None:
                embed2 = discord.Embed(description=f"**This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}lockchannel [channel] [role name]``**",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            role = discord.utils.get(ctx.guild.roles, name=roleName)
            if not role:
                embed3 = discord.Embed(title="No Such Role Found!",color=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

            overwrite = channel.overwrites_for(role)
            if overwrite.send_messages == False:
                embed4 = discord.Embed(description=f"{channel.mention} Channel Is Already Locked!",color=0x0000ff,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed4)
                return

            else:
                perms = channel.overwrites_for(role)
                perms.send_messages = False
                await channel.set_permissions(role, overwrite=perms)
                embed5 = discord.Embed(description=f"Locking {channel.mention} channel!",color=0x00ff00,timestamp=ctx.message.created_at)
                embed6 = discord.Embed(description=f":lock: {channel.mention} Channel Has Been Locked For **{roleName}** Role!",color=0x00ff00,timestamp=ctx.message.created_at)
                msg = await ctx.send(embed=embed5)
                await asyncio.sleep(2)
                await msg.edit(embed=embed6)
                return
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(lockchannel(bot))