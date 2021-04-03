import discord
import asyncio
import time
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
        await msg.edit(content="<==Песня закончилась==>")



            

def setup(bot):
    bot.add_cog(entertainment(bot))