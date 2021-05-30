import configparser
import asyncio
import discord
import sys
import traceback
from discord.ext import commands


#Подключения ####################################################
config = configparser.ConfigParser()
config.read("config.cfg")
configfile = "config.cfg"
#################################################################

#Инициализация языкового пакета##################################
localization = configparser.ConfigParser()
localization.read("localization/" + config["discord"]["Localization"] + ".lang", encoding="cp1251")
print('Localization System loaded')
print(localization["main"]["LocaleLoadMessage"] + " " + localization["LocaleInfo"]["Developer"])
#################################################################

client = commands.Bot(command_prefix = "+") # Ставим префикс команд
client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=localization["main"]["Presence"]))
    print(localization["main"]["OnStartUp"])

initial_extensions = ['modules.voice','modules.weather','modules.info','modules.user','modules.moderation','modules.entertainment', 'modules.langinfo']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} ' + localization["Phrases"]["load"])
        except Exception as e:
            print(localization["main"]["LoadError"] + ' {extension}.', file=sys.stderr)
            traceback.print_exc()

@client.command()
@commands.is_owner()
async def unload(ctx, *, name: str):
    client.remove_cog(name)
    await ctx.channel.send(f'{name} ' + localization["Phrases"]["unload"])
    


client.run(config["discord"]["TOKEN"])