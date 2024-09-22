import discord
import asyncio
from discord.ext import commands
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import textwrap
from botprefix import prefix

class trumptweet(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(aliases=['tt'])
    async def trumptweet(self, ctx, *, text : str = None):

        if not text:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}trumptweet [text]``",color=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)

        else:
            try:
                
                image = Image.open('./Assets/trumptweet.png')
                
                draw = ImageDraw.Draw(image)

                lines = textwrap.wrap(text, width=44)
                font = ImageFont.truetype('./Arial.ttf', 35)

                y_text = 95

                for line in lines:
                    line_width, line_height = font.getsize(line)
                    draw.text((22, y_text), 
                    line, font=font, fill=(0,0,0))
                    y_text += line_height

                buffer = io.BytesIO()
                image.save(buffer, format='png')
                
                buffer.seek(0)
                
                await ctx.send(file=discord.File(buffer, 'myimage.png'))
                return
                
            except Exception as e:
                print(e)



def setup(bot):
	bot.add_cog(trumptweet(bot))