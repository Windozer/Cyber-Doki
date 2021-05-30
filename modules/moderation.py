import discord
import configparser
import asyncio
import sys
from discord.ext import commands
from discord.ext.commands import Bot

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #команда СЕРВИСЫ
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["memberkick"],
                value=localization["Phrases"]["membernotdefined"],
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await channel.send(embed=embed)

        else:
            await member.kick(reason=None)
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["memberkick"],
                value=localization["Phrases"]["member"] + " " + "<@" + str(member.id) + "> " + localization["Phrases"]["kickedfromserver"],
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["playerban"],
                value=localization["Phrases"]["membernotdefined"],
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await channel.send(embed=embed)

        else:
            await member.ban(reason=None)
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["playerban"],
                value=localization["Phrases"]["member"] + " " + "<@" + str(member.id) + "> " + localization["Phrases"]["bannedfromserver"],
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def changenick(self, ctx, nick):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        await ctx.message.author.edit(nick=nick)
        await ctx.send(localization["Phrases"]["nicknamechange"] + f' ' + nick)

def setup(bot):
    bot.add_cog(moderation(bot))