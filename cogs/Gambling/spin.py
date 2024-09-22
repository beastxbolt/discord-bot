import discord
import asyncio
import os
import math
import random
from random import choice, randrange
from asyncio import sleep
from discord.ext import commands
import sqlite3
from sqlite3 import connect
import datetime
import json
from botprefix import prefix


db = connect('./database.db', check_same_thread = False)
cursor = db.cursor()


class spin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def spin(self,ctx, amount : int = None):

        try:
        
            gem = self.bot.get_emoji(710105510984286238)
            tada = self.bot.get_emoji(709752857653673994)

            number = [0.1, 0.3, 0.5, 1.1, 1.4, 1.8, 2.5, 2.5, 1.8, 1.4, 1.1, 0.5, 0.3, 0.1]
            wheelNumber = random.choice(number)
            
            result = cursor.execute(f"SELECT user_id FROM economy WHERE user_id = {ctx.author.id}").fetchone()
            
            if result is None:
                embed = discord.Embed(title=f"**You Are Not Registered!**", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return
                
            if amount is None:
                embed2 = discord.Embed(title=f"This Command Is Used Like This: ``{prefix(self.bot, ctx)[0]}spin [bet amount]``",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed2)
                return
                
            if amount <= 0:
                embed3 = discord.Embed(title=f"Bet Amount Should be Greater than 0!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed3)
                return

            if amount >= 50001:
                embed4 = discord.Embed(title=f"You Cannot Bet More Than 50000 Gems At Once!",colour=0xff0000,timestamp=ctx.message.created_at)
                await ctx.send(embed=embed4)
                return
                
            wallet = cursor.execute(f"SELECT wallet FROM economy WHERE user_id = {ctx.author.id}").fetchone()
            
            if amount > wallet[0]:
                embed5 = discord.Embed(title=f"You Don't Have That Much {gem} In Your Wallet To Bet!", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed5)
                return

            if wheelNumber == 0.1:
                file6 = discord.File('./Assets/Spin0-1.png', filename='Spin0-1.png')
                embed6 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 0.1!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed6.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed6.set_image(url='attachment://Spin0-1.png')
                await ctx.send(file=file6, embed=embed6)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return

            
            if wheelNumber == 0.3:
                file7 = discord.File('./Assets/Spin0-3.png', filename='Spin0-3.png')
                embed7 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 0.3!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed7.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed7.set_image(url='attachment://Spin0-3.png')
                await ctx.send(file=file7, embed=embed7)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return


            if wheelNumber == 0.5:
                file8 = discord.File('./Assets/Spin0-5.png', filename='Spin0-5.png')
                embed8 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 0.5!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed8.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed8.set_image(url='attachment://Spin0-5.png')
                await ctx.send(file=file8, embed=embed8)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return


            if wheelNumber == 1.1:
                file9 = discord.File('./Assets/Spin1-1.png', filename='Spin1-1.png')
                embed9 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 1.1!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed9.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed9.set_image(url='attachment://Spin1-1.png')
                await ctx.send(file=file9, embed=embed9)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return


            if wheelNumber == 1.4:
                file10 = discord.File('./Assets/Spin1-4.png', filename='Spin1-4.png')
                embed10 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 1.4!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed10.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed10.set_image(url='attachment://Spin1-4.png')
                await ctx.send(file=file10, embed=embed10)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return

            if wheelNumber == 1.8:
                file11 = discord.File('./Assets/Spin1-8.png', filename='Spin1-8.png')
                embed11 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 1.8!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed11.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed11.set_image(url='attachment://Spin1-8.png')
                await ctx.send(file=file11, embed=embed11)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return

            if wheelNumber == 2.5:
                file12 = discord.File('./Assets/Spin2-5.png', filename='Spin2-5.png')
                embed12 = discord.Embed(title=f"You Won {math.floor(amount * wheelNumber)} {gem} Gems!\nFor Spinning On 2.5!", colour=0xffff00, timestamp=ctx.message.created_at)
                embed12.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                embed12.set_image(url='attachment://Spin2-5.png')
                await ctx.send(file=file12, embed=embed12)

                cursor.execute("UPDATE economy SET wallet = wallet - ? WHERE user_id = ?", (amount, ctx.author.id))
                db.commit()

                cursor.execute("UPDATE economy SET wallet = wallet + ? WHERE user_id = ?", (math.floor(amount * wheelNumber), ctx.author.id))
                db.commit()

                time = datetime.datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
                cursor.execute("INSERT INTO transactions (reason, money, time, user_id) VALUES (?,?,?,?)", ("Won By Spinning Wheel!", "+" + f"{math.floor(amount * wheelNumber)}", time, ctx.author.id))
                db.commit()
                return

        except Exception as e:
            print(e)


def setup(bot):
	bot.add_cog(spin(bot))