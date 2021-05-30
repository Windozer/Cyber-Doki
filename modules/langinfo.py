import discord
import configparser
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import Bot

class langinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #команда СЕРВИСЫ
    async def langinfo(self, ctx):
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
            name="Language",
            value=localization["LocaleInfo"]["Language"],
            inline=False)
        embed.add_field(
            name="Language Pack Author",
            value=localization["LocaleInfo"]["Developer"],
            inline=False)     
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(langinfo(bot))