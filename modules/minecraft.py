import discord
import asyncio
import requests
import validators
from discord.ext import commands
from skingrabber import skingrabber

class minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def скин(self, ctx, *, nick: str):
        sg = skingrabber()
        skin = sg.get_skin_rendered(user=f"{nick}")
        channel = ctx.message.channel
        embed = discord.Embed(
            color=0x9234EB,
            timestamp=ctx.message.created_at,
        )
        embed.add_field(
            name="Скин пользователя",
            value="Скин игрока загружен!",
            inline=False)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.set_footer(icon_url="https://cdn.discordapp.com/avatars/780510408707932180/89c2612e9227173f8534b47817290427.png", text=f"Обработала Няшка Кибер-Доки!")
        embed.set_image(url=f"{skin}")
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(minecraft(bot))