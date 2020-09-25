import asyncio
import os
import discord
from discord.ext import commands
from settings import token, bot_name, folder_list

client = commands.Bot(command_prefix='+', case_insensitive=True)
client.remove_command("help")


async def change_status():
    await client.wait_until_ready()
    while client.is_ready():
        status = discord.Activity(name=f"+help | {len(client.guilds)} Servers", type=discord.ActivityType.playing)
        await client.change_presence(activity=status)
        await asyncio.sleep(30)

for folder in folder_list:
    print(f"[{bot_name}] ----------------------[ {folder.title()} ]--------------------")
    for filename in os.listdir(f'./{folder}'):
        if filename.endswith('.py'):
            print(f"[{bot_name}] {folder.title()} > {filename[:-3]} > Loaded!")
            client.load_extension(f'{folder}.{filename[:-3]}')

print(f"[{bot_name}] ------------------------------------------------------")

client.loop.create_task(change_status())
client.run(token)
