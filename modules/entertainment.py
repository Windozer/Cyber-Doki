import discord
import asyncio
import time
import urllib
import json
import requests
from random import randint
import configparser
from discord.ext import commands


class entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #команда СЕРВИСЫ
    async def cookie(self, ctx, member:discord.Member):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name=localization["Phrases"]["cookie"],
            value=member.mention + localization["Entertainment"]["cookiemsg"],
            inline=False)        
        embed.set_author(name=localization["main"]["CyberDoki"], icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png")
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
        await channel.send(embed=embed)

    @commands.command()
    async def quote(self, ctx):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json")
        todos = json.loads(response.text)
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name=localization["Phrases"]["quote"],
            value=todos.get('quoteText'),
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(entertainment(bot))