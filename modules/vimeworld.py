import discord
import asyncio
import requests
import validators
import configparser
import sys
import urllib
import traceback
import simplejson as json
from discord.ext import commands

class vimeworld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vинфо(self, ctx):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        configfile = "config.cfg"
        token = config["VimeWorld"]["TOKEN"]
        url = urllib.request.urlopen('https://api.vimeworld.ru/online?token=' + token).read()
        url = json.loads(url)
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="VimeWorld",
            value="Информация о сервере загружена!",
            inline=False)
        embed.add_field(
            name="Общий онлайн",
            value=url.get('total'),
            inline=False)
        embed.add_field(
            name="Лобби",
            value=url.get('separated').get('lobby'),
            inline=False)
        embed.add_field(
            name="Дуэли",
            value=url.get('separated').get('duels'),
            inline=False)
        embed.add_field(
            name="BedWars",
            value=url.get('separated').get('bw'),
            inline=False)
        embed.add_field(
            name="SkyWars",
            value=url.get('separated').get('sw'),
            inline=False)
        embed.add_field(
            name="TNTRun",
            value=url.get('separated').get('tntrun'),
            inline=False)
        embed.add_field(
            name="LuckyWars",
            value=url.get('separated').get('luckywars'),
            inline=False)
        embed.add_field(
            name="MobWars",
            value=url.get('separated').get('mw'),
            inline=False)
        embed.add_field(
            name="HungerGames",
            value=url.get('separated').get('hg'),
            inline=False)
        embed.add_field(
            name="BuildBattle",
            value=url.get('separated').get('bb'),
            inline=False)
        embed.add_field(
            name="Prison",
            value=url.get('separated').get('prison'),
            inline=False)
        embed.add_field(
            name="Murder Mystery",
            value=url.get('separated').get('murder'),
            inline=False)
        embed.add_field(
            name="Bridge",
            value=url.get('separated').get('bridge'),
            inline=False)
        embed.add_field(
            name="JumpLeague",
            value=url.get('separated').get('jumpleague'),
            inline=False)
        embed.add_field(
            name="KitPVP",
            value=url.get('separated').get('kpvp'),
            inline=False)
        embed.add_field(
            name="BlockParty",
            value=url.get('separated').get('bp'),
            inline=False)
        embed.add_field(
            name="ClashPoint",
            value=url.get('separated').get('cp'),
            inline=False)
        embed.add_field(
            name="GunGame",
            value=url.get('separated').get('gg'),
            inline=False)
        embed.add_field(
            name="DeathRun",
            value=url.get('separated').get('dr'),
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cp.vimeworld.ru/tpl/img/vime_logo.png", text=f"Данные получены из VimeWorld Public API")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(vimeworld(bot))