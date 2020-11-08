import discord
import datetime
import math
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='none')
token = "TOKEN_GOES_HERE"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

banned = ["os","sys","math","datetime","discord","discord.ext","...","code","string","math.","sympy"]
replace = [("x","*"),("sin","math.sin"),("cos","math.cos"),("cot","math.cot"),("tan","math.tan")]
@bot.event
async def on_message(message):
    if message.author.bot is False and message.content not in banned:
        original = message.content
        for x in replace:
            message.content = message.content.replace(x[0], x[1])
        try:
            try:
                exec(f"s = {message.content}")
                exec("s")
            except:
                s = eval(message.content)
            if str(s) != message.content or str(math.abs(s)) != message.content:
                await message.channel.send("**"+ original + " = **" + str(s))
        except:
            pass


bot.run(token)
