import discord
import asyncio
import configparser
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command() #команда СЕРВИСЫ
    async def бот(self, ctx):
                config = configparser.ConfigParser()
                config.read("config.cfg")
                configfile = "config.cfg"
                channel = ctx.message.channel
                embed = discord.Embed(
                    color=0x9234EB,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(
                    name="Привет!",
                    value=f"Я бот, мой разработчик " + config["discord"]["DeveloperID"] + ", пока-что я обладаю небольшим функционалом. Пока что я могу показать тебе погоду, а остальные функции и команды можно узнать прописав команду +помощь",
                    inline=False)    
                embed.set_author(name=f"Я - Кибер-Доки!", icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png")
                embed.set_footer(text=f"Запрос обработан")
                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))