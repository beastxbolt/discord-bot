import discord,random
from discord.ext import commands
import json
from botprefix import prefix

class bigtext(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        

    @commands.command()
    async def bigtext(self,ctx,*,word : str = None):
        l = [0X16A085,0X45EBEB,0X44EC7C,0XCA36F1,0XF5B041,0X2874A6,0XEBDEF0,0X00ff00,0X26F1B1,0X2874A6,0XF08080,0XFA8072]
        a = random.choice(l)

        word = word.lower()
        
        if not word:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}bigtext [word]``", colour=a, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)
            return


        else:
            lis = []
            for l in word:
                str(l)
                l.lower()
                if l == " ":
                    lis.append(" ")
                    continue
                lis.append(f":regional_indicator_{l}:")
            
            big= " ".join([l for l in lis])
     
            e = discord.Embed(title=big,colour=a,timestamp=ctx.message.created_at)
            e.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=e)

            

def setup(bot):
    bot.add_cog(bigtext(bot))
        