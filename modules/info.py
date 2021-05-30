import discord
import asyncio
import configparser
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command() 
    async def doki(self, ctx):
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
                    name=localization["BotInfo"]["iamcyberdoki"],
                    value=localization["Phrases"]["mydevis"] + " " + config["discord"]["DeveloperID"] + localization["BotInfo"]["botdescription"],
                    inline=False)    
                embed.add_field(
                    name=localization["BotInfo"]["weongithub"],
                    value=localization["BotInfo"]["githubdescription"] + f" [GitHub](https://github.com/Windozer/Cyber-Doki)",
                    inline=False)    
                embed.set_author(name=localization["BotInfo"]["iamcyberdoki"], icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png")
                embed.set_footer(text=localization["Phrases"]["ProcessedMessage"])
                await channel.send(embed=embed)
           

def setup(bot):
    bot.add_cog(info(bot))