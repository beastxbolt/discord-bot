import discord
from discord.ext import commands
import asyncio
import sqlite3
from sqlite3 import connect
import random
from random import randrange
from botprefix import prefix


db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()


class giftcode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    
    @commands.group()
    @commands.is_owner()
    async def giftcode(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}giftcode [sub command]``",colour=0xff0000,timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)


    @giftcode.command()
    async def generate(self, ctx, value : int = None):

        a = randrange(10000000, 9999999999)
        b = randrange(10000000, 9999999999)
        c = randrange(10000000, 9999999999)
        d = randrange(10000000, 9999999999)
        e = randrange(10000000, 9999999999)

        try:

            if value is None:
                embed3 = discord.Embed(title="Please Enter Giftcode Value!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

            giftcodeCheck = cursor.execute(f"SELECT code FROM giftcode WHERE code = {a}").fetchone()

            if giftcodeCheck is None:
                cursor.execute("INSERT INTO giftcode (code, value) VALUES (?,?)", (a, value))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode Has Been Successfully Generated!\n**Giftcode** - ``{a}``\n**Value** - ``{value}`` Gems")
                return

            giftcodeCheck2 = cursor.execute(f"SELECT code FROM giftcode WHERE code = {b}").fetchone()

            if giftcodeCheck2 is None:
                cursor.execute("INSERT INTO giftcode (code, value) VALUES (?,?)", (b, value))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode Has Been Successfully Generated!\n**Giftcode** - ``{b}``\n**Value** - ``{value}`` Gems")
                return

            giftcodeCheck3 = cursor.execute(f"SELECT code FROM giftcode WHERE code = {c}").fetchone()

            if giftcodeCheck3 is None:
                cursor.execute("INSERT INTO giftcode (code, value) VALUES (?,?)", (c, value))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode Has Been Successfully Generated!\n**Giftcode** - ``{c}``\n**Value** - ``{value}`` Gems")
                return

            giftcodeCheck4 = cursor.execute(f"SELECT code FROM giftcode WHERE code = {d}").fetchone()

            if giftcodeCheck4 is None:
                cursor.execute("INSERT INTO giftcode (code, value) VALUES (?,?)", (d, value))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode Has Been Successfully Generated!\n**Giftcode** - ``{d}``\n**Value** - ``{value}`` Gems")
                return

            giftcodeCheck5 = cursor.execute(f"SELECT code FROM giftcode WHERE code = {e}").fetchone()

            if giftcodeCheck5 is None:
                cursor.execute("INSERT INTO giftcode (code, value) VALUES (?,?)", (e, value))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode Has Been Successfully Generated!\n**Giftcode** - ``{e}``\n**Value** - ``{value}`` Gems")
                return

            else:
                await ctx.send(f"{ctx.author.mention}, All Giftcode Checks Exist, Please Try Again!")
                

        except Exception as e:
            print(e)



    @giftcode.command()
    async def update(self, ctx, code : int = None, value : int = None):

        try:
            if code is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ```++giftcode update [code] [value]```",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            if value is None:
                embed2 = discord.Embed(title="Please Enter Giftcode Value!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return

            giftcodeCheck = cursor.execute(f"SELECT code FROM giftcode WHERE code = {code}").fetchone()

            if giftcodeCheck is None:
                await ctx.send(f"{ctx.author.mention}, Giftcode Not Found!")
                return

            else:
                cursor.execute("UPDATE giftcode SET value = ? WHERE code = ?", (value, code))
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode - ``{code}`` Has Been Updated!")
                return
        except Exception as e :
            print(e)


    @giftcode.command()
    async def delete(self, ctx, code : int = None):

        try:

            if code is None:
                embed = discord.Embed(title=f"This Command Is Used Like This: ```++giftcode delete [code]```",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            giftcodeCheck = cursor.execute(f"SELECT code FROM giftcode WHERE code = {code}").fetchone()

            if giftcodeCheck is None:
                await ctx.send(f"{ctx.author.mention}, Giftcode Not Found!")
                return

            else:
                cursor.execute(f"DELETE FROM giftcode WHERE code = {code}")
                db.commit()
                await ctx.send(f"{ctx.author.mention}, Giftcode - ``{code}`` Has Been Deleted!")
                return
        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(giftcode(bot))