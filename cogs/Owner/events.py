import discord
from discord.ext import commands
import asyncio
import math
import random
from random import randrange
import sqlite3
from sqlite3 import connect
from discord.utils import get
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import io
from io import BytesIO
import time
import json
from botprefix import prefix


db = connect('./database.db', check_same_thread=False)
cursor = db.cursor()

invites = {}

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Is Ready!")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f".help"))
        for guild in self.bot.guilds:
            invites[guild.id] = await guild.invites()



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title="There Is No Such Command!",color=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description=f"**{error}**", colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(title="This is a Owner-Only command!",colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed)
            return

        if isinstance(error,commands.BadArgument):
            embed4 = discord.Embed(title="Check Your Argument and Try Again!",colour=0xff0000, timestamp=ctx.message.created_at)
            await ctx.send(embed=embed4)
            return




    @commands.Cog.listener()
    async def on_message(self, message):

        tada = self.bot.get_emoji(709752857653673994)
        levelup_emoji = self.bot.get_emoji(744183424688062576)

        xp_add = randrange(1, 4)

        async def lvlnone():
            cursor.execute("UPDATE experience SET level = ? WHERE user_id = ? AND guild_id = ?", (int(level_start + 1), message.author.id, message.guild.id))
            db.commit()

            cursor.execute("UPDATE experience SET xp = ? WHERE user_id = ? AND guild_id = ?", (0, message.author.id, message.guild.id))
            db.commit()

            await message.channel.send(f"GG! {message.author.mention}, you just advanced to Level **{level_start + 1}**!{tada}")
            return

        result = cursor.execute(f"SELECT user_id, guild_id FROM experience WHERE user_id = {message.author.id} AND guild_id = {message.guild.id}").fetchone()

        if result is None:
            if not message.author.bot:
                cursor.execute("INSERT INTO experience(user_id, guild_id, xp, level, totalxp) VALUES (?,?,?,?,?)", (message.author.id, message.guild.id, xp_add, 0, xp_add))
                db.commit()

            checkStatus = cursor.execute(f"SELECT status FROM config_leveling WHERE guild_id = {message.guild.id}").fetchone()

            if checkStatus is None:
                cursor.execute("INSERT INTO config_leveling (status, guild_id) VALUES (?,?)", ("enabled", message.guild.id))
                db.commit()
                return

        else:

            checkStatus = cursor.execute(f"SELECT status FROM config_leveling WHERE guild_id = {message.guild.id}").fetchone()

            if checkStatus[0] == "disabled":
                return

            if checkStatus[0] == "enabled":

                cursor.execute("UPDATE experience SET xp = xp + ? WHERE user_id = ? AND guild_id = ?", (xp_add, message.author.id, message.guild.id))
                db.commit()

                cursor.execute("UPDATE experience SET totalxp = totalxp + ? WHERE user_id = ? AND guild_id = ?", (xp_add, message.author.id, message.guild.id))
                db.commit()

                result2 = cursor.execute(f"SELECT xp, level FROM experience WHERE user_id = {message.author.id} AND guild_id = {message.guild.id}").fetchone()

                xp_start = int(result2[0])
                level_start = int(result2[1])
                xp_end = math.floor(5 * (level_start ^ 2) + 150 * level_start + 250)


                levelup = cursor.execute(f"SELECT channel_id FROM levelups WHERE guild_id = {message.guild.id}").fetchone()

                if xp_end < xp_start:

                    if levelup is None:
                        await lvlnone()


                    if levelup is not None:
                        levelupchannel = self.bot.get_channel(id=levelup[0].__int__())

                        if not levelupchannel:
                            await lvlnone()

                        else:

                            cursor.execute("UPDATE experience SET level = ? WHERE user_id = ? AND guild_id = ?", (int(level_start + 1), message.author.id, message.guild.id))
                            db.commit()

                            cursor.execute("UPDATE experience SET xp = ? WHERE user_id = ? AND guild_id = ?", (0, message.author.id, message.guild.id))
                            db.commit()

                            await levelupchannel.send(f"GG! {message.author.mention}, you just advanced to Level **{level_start + 1}**! {levelup_emoji}")
                            return




    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        for role in guild.roles:
            if role.name == "8-BIT Muted":
                return

            else:
                permissions = discord.Permissions(administrator=False, view_audit_log=False, manage_guild=False, manage_roles=False, manage_channels=False, kick_members=False, ban_members=False, create_instant_invite=True, change_nickname=True, manage_nicknames=False, manage_webhooks=False, send_messages=False, send_tts_messages=False, manage_messages=False, embed_links=False, attach_files=False, read_message_history=True, use_external_emojis=False, add_reactions=False, connect=False, speak=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
        await guild.create_role(name="8-BIT Muted", colour=discord.Colour.from_rgb(1, 1, 1) , mentionable=False, permissions=permissions)
        await asyncio.sleep(2)

        role2 = discord.utils.get(guild.roles, name="8-BIT Muted")

        for channel in guild.text_channels:

            perms = channel.overwrites_for(role2)
            perms.create_instant_invite = True
            perms.manage_channels = False
            perms.manage_permissions = False
            perms.manage_webhooks = False
            perms.read_messages = True
            perms.send_messages = False
            perms.send_tts_messages = False
            perms.manage_messages = False
            perms.embed_links = False
            perms.attach_files = False
            perms.read_message_history = True
            perms.use_external_emojis = False
            perms.add_reactions = False
            await channel.set_permissions(role2, overwrite=perms)

        role3 = discord.utils.get(guild.roles, name="8-BIT Muted")

        for channel in guild.voice_channels:

            perms2 = channel.overwrites_for(role3)
            perms2.create_instant_invite = True
            perms2.manage_channels = False
            perms2.manage_permissions = False
            perms2.manage_webhooks = False
            perms2.view_channel = True
            perms2.connect = False
            perms2.speak = False
            perms2.stream = False
            perms2.mute_members = False
            perms2.deafen_members = False
            perms2.move_members = False
            perms2.use_voice_activation = False
            perms2.priority_speaker = False
            await channel.set_permissions(role3, overwrite=perms2)



    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):

        role3 = discord.utils.get(channel.guild.roles, name="8-BIT Muted")

        perms3 = channel.overwrites_for(role3)
        perms3.create_instant_invite = True
        perms3.manage_channels = False
        perms3.manage_permissions = False
        perms3.manage_webhooks = False
        perms3.read_messages = True
        perms3.send_messages = False
        perms3.send_tts_messages = False
        perms3.manage_messages = False
        perms3.embed_links = False
        perms3.attach_files = False
        perms3.read_message_history = True
        perms3.use_external_emojis = False
        perms3.add_reactions = False
        await channel.set_permissions(role3, overwrite=perms3)

        role4 = discord.utils.get(channel.guild.roles, name="8-BIT Muted")


        perms4 = channel.overwrites_for(role4)
        perms4.create_instant_invite = True
        perms4.manage_channels = False
        perms4.manage_permissions = False
        perms4.manage_webhooks = False
        perms4.view_channel = True
        perms4.connect = False
        perms4.speak = False
        perms4.stream = False
        perms4.mute_members = False
        perms4.deafen_members = False
        perms4.move_members = False
        perms4.use_voice_activation = False
        perms4.priority_speaker = False
        await channel.set_permissions(role4, overwrite=perms4)


    @commands.Cog.listener()
    async def on_member_join(self, member):

        async def invitefunc():
            def find_invite_by_code(invite_list, code):
                for inv in invite_list:
                    if inv.code == code:
                        return inv

            channelID = cursor.execute(f"SELECT channel_id FROM invitation WHERE guild_id = {member.guild.id}").fetchone()
            statusCheck = cursor.execute(f"SELECT status FROM invitation WHERE guild_id = {member.guild.id}").fetchone()
            if channelID is None:
                 return

            if statusCheck[0] == "disabled":
                return

            channel = self.bot.get_channel(channelID[0].__int__())

            if not channel:
                return

            invites_before_join = invites[member.guild.id]
            invites_after_join = await member.guild.invites()


            for invite in invites_before_join:

                if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:

                    await channel.send(f"**{member.mention} joined**. Invited by **{invite.inviter.display_name}** (**{find_invite_by_code(invites_after_join, invite.code).uses}** invites)")
                    return

            else:
                await channel.send(f"I can't figure out how {member.mention} joined the server.")
                return


        async def welcomefunc():
            channelID2 = cursor.execute(f"SELECT channel_id FROM join_leave WHERE guild_id = {member.guild.id}").fetchone()
            statusCheck2 = cursor.execute(f"SELECT status FROM join_leave WHERE guild_id = {member.guild.id}").fetchone()
            if channelID2 is None:
                    return

            if statusCheck2[0] == "disabled":
                return

            channel = self.bot.get_channel(channelID2[0].__int__())

            if not channel:
                return

            else:
                tada = self.bot.get_emoji(709752857653673994)

                image = Image.open('./Assets/welcome.jpg')
                draw = ImageDraw.Draw(image)

                AVATAR_SIZE = 256
                avatar_asset = member.avatar_url_as(format='png', size=AVATAR_SIZE)
                buffer_avatar = io.BytesIO()
                await avatar_asset.save(buffer_avatar)
                buffer_avatar.seek(0)

                avatar_image = Image.open(buffer_avatar)
                avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE))
                circle_image = Image.new('L', (AVATAR_SIZE, AVATAR_SIZE))
                circle_draw = ImageDraw.Draw(circle_image)
                circle_draw.ellipse((0, 0, AVATAR_SIZE, AVATAR_SIZE), fill=255)
                avatar_image.putalpha(circle_image)
                image.paste(avatar_image, (23, 38), circle_image)

                text = "Welcome To The Server!"
                text2 = member.name
                text3 = "You Are The"
                text4 = f"{len(member.guild.members)} Member!"
                font = ImageFont.truetype('./Arial.ttf', 35)
                draw.text((345, 50), text, fill=(255,255,255,255), font=font)
                draw.text((345, 125), text2, fill=(255,255,255,255), font=font)
                draw.text((345, 167), text3, fill=(255,255,255,255), font=font)
                draw.text((345, 207), text4, fill=(255,255,255,255), font=font)

                buffer = io.BytesIO()
                image.save(buffer, format='png')

                buffer.seek(0)

                embed = discord.Embed(description=f"**{member.mention} Welcome To {member.guild.name} {tada}\nHave A Great Time Here!**", colour=0x0000ff)
                embed.set_image(url='attachment://welcome.jpg')

                await channel.send(file=discord.File(buffer, 'welcome.jpg'), embed=embed)
                return

        await invitefunc()
        await welcomefunc()



    @commands.Cog.listener()
    async def on_member_remove(self, member):

        channelID = cursor.execute(f"SELECT channel_id FROM join_leave WHERE guild_id = {member.guild.id}").fetchone()
        if channelID is None:
            return

        else:
            channel = self.bot.get_channel(channelID[0].__int__())
            embed = discord.Embed(description=f"**{member.mention} Has Left The Server.\nHope You'll Be Back Soon!**", colour=0xffff00)
            embed.set_author(name=member)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"We Now Have {len(member.guild.members)} Members!")

            await channel.send(embed=embed)
            return


    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        invites[invite.guild.id] = await invite.guild.invites()

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        invites[invite.guild.id] = await invite.guild.invites()


def setup(bot):
    bot.add_cog(Events(bot))
