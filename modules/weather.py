import discord
import asyncio
import requests
import validators
import configparser
from discord.ext import commands

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['Погода','weather','pogoda','пОгода']) # Команда ПОГОДА
    async def погода(self, ctx, *, city: str):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        configfile = "config.cfg"
        api_key = config["OpenWeather"]["TOKEN"]
        base_url = config["OpenWeather"]["URL"]
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":

                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]

                embed = discord.Embed(
                    title=f"Город - {city_name}",
                    color=0x9234EB,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(
                    name="Температура(C)",
                    value=f"**{current_temperature_celsiuis}°C**",
                    inline=False)
                embed.add_field(
                    name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
                embed.add_field(
                    name="Атмосферное давление(hPa)",
                    value=f"**{current_pressure}hPa**",
                    inline=False)
                embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
                embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")

                await channel.send(embed=embed)

        else:
                await channel.send(
                    f"Ня, по твоему запросу я не смогла ничего найти!")

def setup(bot):
    bot.add_cog(weather(bot))