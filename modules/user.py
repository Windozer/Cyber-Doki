import discord
import asyncio
import requests
import validators
import random
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import Bot

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def аватарка(self, ctx, member: discord.Member=None):
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Аватар пользователя",
                value="Ваш аватар успешно загружен!",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            embed.set_image(url=ctx.message.author.avatar_url)
            await channel.send(embed=embed)

        else:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name="Аватар пользователя",
                value="Аватар " + "<@" + str(member.id) + ">",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

    @commands.command()
    async def пользователь(self, ctx, member:discord.Member = None, guild: discord.Guild = None):
        if member == None:
            emb = discord.Embed(title="Информация о пользователе", color=0x9234EB)
            emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
            emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
            emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
            emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role.mention}",inline=False)
            emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.set_thumbnail(url=ctx.message.author.avatar_url)
            emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await ctx.send(embed = emb)
        else:
            emb = discord.Embed(title="Информация о пользователе", color=0x9234EB)
            emb.add_field(name="Имя пользователя:", value="<@" + str(member.id) + ">",inline=False)
            emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
            emb.add_field(name="Статус:", value=member.activity,inline=False)
            emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
            emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
            await ctx.send(embed = emb)

    @commands.command()
    async def посчитай(self, ctx, operation, *nums):
        if operation not in ['+', '-', '*', '/']:
            await ctx.send('Пример запроса: +посчитай + 1 1')
        var = f' {operation} '.join(nums)
        await ctx.send(f'{var} = {eval(var)}')

    @commands.command()
    async def удалисообщения(self, ctx, user: discord.Member):
        await ctx.channel.purge(limit=None, check=lambda m: m.author==user)
        await ctx.channel.send(f'Ня, я очистила сообщения ' + f"<@" + str(user.id) + f">")

    @commands.command()
    async def сервер(self, ctx):
        emb = discord.Embed(title="Информация о сервере", color=0x9234EB)
        emb.add_field(name="Имя:", value=ctx.message.guild.name,inline=False)
        emb.add_field(name="Количество участников:", value=ctx.message.guild.member_count,inline=False)
        emb.add_field(name="Айди сервера:", value=ctx.message.guild.id,inline=False)
        emb.add_field(name="Регион:", value=ctx.message.guild.region,inline=False)
        emb.add_field(name="Сервер был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.guild.icon_url)
        emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
        await ctx.send(embed = emb)

    @commands.command()
    async def помощь(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(
            title="Команды",
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="+сервер",
            value="Отображение информации о сервере",
            inline=False)
        embed.add_field(
            name="+пользователь (пользователь)",
            value="Отображение информации о пользователе",
            inline=False)
        embed.add_field(
            name="+аватарка (пользователь)",
            value="Отображение информации о пользователе",
            inline=False)
        embed.add_field(
            name="+пароль",
            value="Бот генерирует пароль из 11 символов для вас и отправляет вам в ЛС",
            inline=False)
        embed.add_field(
            name="+vинфо",
            value="Отображение информации о онлайне серверов VimeWorld",
            inline=False)
        embed.add_field(
            name="+рандом",
            value="Отображение псевдо-случайного числа",
            inline=False)
        embed.add_field(
            name="+печенька (пользователь)",
            value="Отправляет уведомление о получении печеньки пользователю",
            inline=False)
        embed.add_field(
            name="+цитата",
            value="Отображение случайной цитаты",
            inline=False)
        embed.add_field(
            name="+кик (пользователь)",
            value="Изгнание пользователя с сервера",
            inline=False)
        embed.add_field(
            name="+бан (пользователь)",
            value="Блокировка доступа к серверу",
            inline=False)
        embed.add_field(
            name="+ник (ник)",
            value="Изменение своего ника на сервере",
            inline=False)
        embed.add_field(
            name="+голос setup",
            value="Запуск установки голосового канала",
            inline=False)
        embed.add_field(
            name="+голос блок (пользователь)",
            value="Блокировка доступа к каналу",
            inline=False)
        embed.add_field(
            name="+голос разблок (пользователь)",
            value="Разблокировка доступа к каналу",
            inline=False)
        embed.add_field(
            name="+голос разрешить (пользователь)",
            value="Разблокировать игроку доступ к каналу",
            inline=False)
        embed.add_field(
            name="+голос запретить (пользователь)",
            value="Запретить игроку к каналу",
            inline=False)
        embed.add_field(
            name="+голос лимит (цифра)",
            value="Установка лимита пользователей в канале",
            inline=False)
        embed.add_field(
            name="+голос название (название)",
            value="Изменен",
            inline=False)
        embed.add_field(
            name="+голос права",
            value="Получение прав администрирования над каналом (Если владелец вышел из канала)",
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
        await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    async def пароль(self, ctx):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = int('1')
        length = int('11')
        channel = ctx.message.channel
        for n in range(number):
            password =''
            for i in range(length):
                password += random.choice(chars)
            await ctx.message.author.send(password)
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Генерация случайного пароля",
            value="Пароль был отправлен тебе!",
            inline=False)        
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=f"P.S: Кибер-Доки не сохраняет сгенерированные пароли!")
        await channel.send(embed=embed)
    

def setup(bot):
    bot.add_cog(user(bot))