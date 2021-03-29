import discord
import asyncio
import sys
from discord.ext import commands
from discord.ext.commands import Bot

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #команда СЕРВИСЫ
    @commands.has_permissions(kick_members=True)
    async def кик(self, ctx, member: discord.Member=None):
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Изгнание игрока с сервера",
                value="Не упомянут игрок!",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await channel.send(embed=embed)

        else:
            await member.kick(reason=None)
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Изгнание игрока с сервера",
                value="Игрок " + "<@" + str(member.id) + "> изгнан с сервера!",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    @commands.has_permissions(kick_members=True)
    async def бан(self, ctx, member: discord.Member=None):
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Блокировка игрока",
                value="Не упомянут игрок!",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await channel.send(embed=embed)

        else:
            await member.ban(reason=None)
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Блокировка игрока",
                value="Игрок " + "<@" + str(member.id) + "> заблокирован на сервере!",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(moderation(bot))