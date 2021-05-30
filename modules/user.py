import discord
import configparser
import asyncio
import requests
import validators
import json
import random
from discord.ext import commands
from datetime import datetime
from discord.ext.commands import Bot

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getavatar(self, ctx, member: discord.Member=None):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        if member is None:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                    timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["useravatar"],
                value=localization["Users"]["avatarloadedmsg"],
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            embed.set_image(url=ctx.message.author.avatar_url)
            await channel.send(embed=embed)

        else:
            channel = ctx.message.channel
            embed = discord.Embed(
                color=0x9234EB,
                timestamp=ctx.message.created_at,
            )
            embed.add_field(
                name=localization["Phrases"]["useravatar"],
                value=localization["Phrases"]["avatar"] + " " + "<@" + str(member.id) + ">",
                inline=False)
            embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            embed.set_image(url=member.avatar_url)
            await channel.send(embed=embed)

    @commands.command()
    async def user(self, ctx, member:discord.Member = None, guild: discord.Guild = None):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        if member == None:
            emb = discord.Embed(title=localization["Phrases"]["informationofuser"], color=0x9234EB)
            emb.add_field(name=localization["User"]["name"], value=ctx.message.author.display_name,inline=False)
            emb.add_field(name=localization["User"]["id"], value=ctx.message.author.id,inline=False)
            emb.add_field(name=localization["User"]["state"], value=ctx.message.author.activity,inline=False)
            emb.add_field(name=localization["User"]["serverrole"], value=f"{ctx.message.author.top_role.mention}",inline=False)
            emb.add_field(name=localization["User"]["accountcreated"], value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.set_thumbnail(url=ctx.message.author.avatar_url)
            emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await ctx.send(embed = emb)
        else:
            emb = discord.Embed(title=localization["Phrases"]["informationofuser"], color=0x9234EB)
            emb.add_field(name=localization["User"]["name"], value="<@" + str(member.id) + ">",inline=False)
            emb.add_field(name=localization["User"]["id"], value=member.id,inline=False)
            emb.add_field(name=localization["User"]["state"], value=member.activity,inline=False)
            emb.add_field(name=localization["User"]["serverrole"], value=f"{member.top_role.mention}",inline=False)
            emb.add_field(name=localization["User"]["accountcreated"], value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
            emb.set_thumbnail(url=member.avatar_url)
            emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
            emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
            await ctx.send(embed = emb)

    @commands.command()
    async def calculate(self, ctx, operation, *nums):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        if operation not in ['+', '-', '*', '/']:
            await ctx.send('Пример запроса: +посчитай + 1 1')
        var = f' {operation} '.join(nums)
        await ctx.send(f'{var} = {eval(var)}')

    @commands.command()
    async def delmessage(self, ctx, user: discord.Member):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        await ctx.channel.purge(limit=None, check=lambda m: m.author==user)
        await ctx.channel.send(f'Ня, я очистила сообщения ' + f"<@" + str(user.id) + f">")

    @commands.command()
    async def server(self, ctx):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        emb = discord.Embed(title=localization["Phrases"]["informationofserver"], color=0x9234EB)
        emb.add_field(name=localization["User"]["name"], value=ctx.message.guild.name,inline=False)
        emb.add_field(name=localization["User"]["membersnumber"], value=ctx.message.guild.member_count,inline=False)
        emb.add_field(name=localization["User"]["serverid"], value=ctx.message.guild.id,inline=False)
        emb.add_field(name=localization["User"]["region"], value=ctx.message.guild.region,inline=False)
        emb.add_field(name=localization["User"]["servercreatedas"], value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.guild.icon_url)
        emb.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        emb.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
        await ctx.send(embed = emb)

    @commands.command()
    async def help(self, ctx):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
        channel = ctx.message.channel
        embed = discord.Embed(
            title="Команды",
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="+server",
            value="Отображение информации о сервере",
            inline=False)
        embed.add_field(
            name="+user (пользователь)",
            value="Отображение информации о пользователе",
            inline=False)
        embed.add_field(
            name="+getavatar (пользователь)",
            value="Отображение информации о пользователе",
            inline=False)
        embed.add_field(
            name="+passgen",
            value="Бот генерирует пароль из 11 символов для вас и отправляет вам в ЛС",
            inline=False)
        embed.add_field(
            name="+cookie (пользователь)",
            value="Отправляет уведомление о получении печеньки пользователю",
            inline=False)
        embed.add_field(
            name="+quote",
            value="Отображение случайной цитаты",
            inline=False)
        embed.add_field(
            name="+kick (пользователь)",
            value="Изгнание пользователя с сервера",
            inline=False)
        embed.add_field(
            name="+ban (пользователь)",
            value="Блокировка доступа к серверу",
            inline=False)
        embed.add_field(
            name="+changenick (ник)",
            value="Изменение своего ника на сервере",
            inline=False)
        embed.add_field(
            name="+voice setup",
            value="Запуск установки голосового канала",
            inline=False)
        embed.add_field(
            name="+voice lock (пользователь)",
            value="Блокировка доступа к каналу",
            inline=False)
        embed.add_field(
            name="+voice unlock (пользователь)",
            value="Разблокировка доступа к каналу",
            inline=False)
        embed.add_field(
            name="+voice allow (пользователь)",
            value="Разблокировать игроку доступ к каналу",
            inline=False)
        embed.add_field(
            name="+voice deny (пользователь)",
            value="Запретить игроку к каналу",
            inline=False)
        embed.add_field(
            name="+voice limit (цифра)",
            value="Установка лимита пользователей в канале",
            inline=False)
        embed.add_field(
            name="+voice name (название)",
            value="Изменение имени канала",
            inline=False)
        embed.add_field(
            name="+voice rights",
            value="Получение прав администрирования над каналом (Если владелец вышел из канала)",
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=localization["Phrases"]["ProcessedMessage"])
        await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    async def passgen(self, ctx):
        config = configparser.ConfigParser()
        config.read("config.cfg")
        localization = configparser.ConfigParser()
        localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
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
            name=localization["User"]["passgentitle"],
            value=localization["User"]["passgentext"],
            inline=False)        
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text=localization["User"]["passgennotice"])
        await channel.send(embed=embed)

    @commands.command() #команда СЕРВИСЫ
    async def nitrogen(self, ctx):
        chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        number = int('1')
        length = int('16')
        for n in range(number):
            nitrolink =''
            for i in range(length):
                nitrolink += random.choice(chars)
            await ctx.send(f'https://discord.gift/{nitrolink}')
    

def setup(bot):
    bot.add_cog(user(bot))