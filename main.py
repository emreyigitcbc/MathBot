import discord
import datetime
import math
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='none')
token = "YOUR TOKEN GOES HERE"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

banned = ["os","sys","math","datetime","discord","discord.ext"]
@bot.event
async def on_message(message):
    if message.author.bot is False and message.content not in banned:
        try:
            try:
                exec(f"s = {message.content}")
                exec("s")
            except:
                s = eval(message.content)
            if str(s) != message.content:
                await message.channel.send(message.content + " = " + str(s))
        except:
            pass


bot.run(token)
