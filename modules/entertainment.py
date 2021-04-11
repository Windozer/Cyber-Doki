import discord
import asyncio
import time
import urllib
import json
import requests
from bs4 import BeautifulSoup
from random import randint
import configparser
from discord.ext import commands


class entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #команда СЕРВИСЫ
    async def рандом(self, ctx):
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Рандом",
                value="Выпало число " + str(randint(0, 12)),
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    async def броулстарс(self, ctx):
        msg = await ctx.send("Песня про Броуууул Старс")
        time.sleep(3)
        await msg.edit(content="Депрессивный хит")
        time.sleep(2)
        await msg.edit(content="Леон, Шелли, Пайпер, Френк, Пем, Тара... ВОРОН!!!")  
        time.sleep(4)
        await msg.edit(content="Баю-Баю, засыпай")
        time.sleep(2)
        await msg.edit(content="Шелли пападают в рай")
        time.sleep(2)
        await msg.edit(content="Не ультуй, не стреляй")
        time.sleep(2)
        await msg.edit(content="Не ультуй, не стреляй")
        time.sleep(2)
        await msg.edit(content="Я тебя не позову")
        time.sleep(2)
        await msg.edit(content="Не помню я твой ID")
        time.sleep(2)
        await msg.edit(content="И как мы вчера и где")
        time.sleep(2)
        await msg.edit(content="И мы ведь даже не в ШД")
        time.sleep(2)
        await msg.edit(content="Мы спутались под ГемГреб")
        time.sleep(2)
        await msg.edit(content="Мы спутались, как в ШД")
        time.sleep(2)
        await msg.edit(content="Ты донила на Рико")
        time.sleep(2)
        await msg.edit(content="Но выпал только Леон")
        time.sleep(2)
        await msg.edit(content="Слезы потекут рекой")
        time.sleep(2)
        await msg.edit(content="Принимай, подушка")
        time.sleep(2)
        await msg.edit(content="Шелли тихо подойдет и скажет Леону")
        time.sleep(3)
        await msg.edit(content="Слезы потекут рекой")
        time.sleep(2)
        await msg.edit(content="Принимай, Эль Примо")
        time.sleep(2)
        await msg.edit(content="Шелли тихо подойдет и скажет на ушко")
        time.sleep(3)
        await msg.edit(content="Баю-бай, засыпай")
        time.sleep(2)
        await msg.edit(content="Шелли попадают в рай")
        time.sleep(2)
        await msg.edit(content="Не ультуй, не стреляй")
        time.sleep(2)
        await msg.edit(content="Не ультуй, не стреляй")
        time.sleep(2)
        await msg.edit(content="0_0 - Песня закончилась!")

    @commands.command() #команда СЕРВИСЫ
    async def печенька(self, ctx, member:discord.Member):
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Печенька",
            value=member.mention + ", ты получил печеньку!",
            inline=False)        
        embed.set_author(name=f"Кибер-Доки", icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png")
        embed.set_footer(text=f"Запрос обработан")
        await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    async def броулстарс1(self, ctx):
        msg = await ctx.send("Песня про Броуууул Старс")
        time.sleep(3)
        await msg.edit(content="Депрессивный хит")
        time.sleep(2)
        await msg.edit(content="Она хочет взять ремень, Удалить бравл старс (Стааарс)")  
        time.sleep(4)
        await msg.edit(content="Получай ульту, из дома бегу (бегу-бегу)")
        time.sleep(3)
        await msg.edit(content="Из дома бегу, получй ульту (ппп)")
        time.sleep(2)
        await msg.edit(content="Беру телефон, И иду катать!")
        time.sleep(2)
        await msg.edit(content="0_0 - Песня закончилась!")

    @commands.command()
    async def кот(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Котики",
            value="Картинка с котиком загружена!",
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_image(url='https://cataas.com/cat')
        embed.set_footer(text=f"Картинка загружена с CATAAS")
        await channel.send(embed=embed)

    @commands.command()
    async def цитата(self, ctx):
        response = requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json")
        todos = json.loads(response.text)
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Цитата",
            value=todos.get('quoteText'),
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=f"Запрос обработан!")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(entertainment(bot))