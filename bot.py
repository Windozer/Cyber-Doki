import configparser
import asyncio
import discord
from discord.ext import commands


#Подключения ####################################################
config = configparser.ConfigParser()
config.read("config.cfg")
configfile = "config.cfg"
print('[1-3] Подключение файла конфигурации и настройка OpenWeather прошла успешно!')
#################################################################

client = commands.Bot(command_prefix = "+") # Ставим префикс команд
client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "Ня, я слежу за " + str(len(client.guilds)) + " серверами!"))
    print('✅Бот запущен!')

initial_extensions = ['modules.voice']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

initial_extensions = ['modules.weather']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

initial_extensions = ['modules.info']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

initial_extensions = ['modules.vimeworld']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

initial_extensions = ['modules.user']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

initial_extensions = ['modules.minecraft']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} подгружен!')
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()



@client.command()
@commands.is_owner()
async def отгрузить(ctx, *, name: str):
    client.remove_cog(name)
    await ctx.channel.send(f'{name} ' + 'отгружен!')
    


client.run(config["discord"]["TOKEN"])