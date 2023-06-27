from asyncore import loop
import random
import time
import os
import discord
import keep_alive
from discord.ext import commands


tostop = 0

intents = discord.Intents.all()

# TOKEN = os.environ["Token"] # if you want to create env file
tecno = commands.Bot(command_prefix=".", intents=intents)


@tecno.event
async def on_connect():
    await tecno.change_presence(activity=discord.Streaming(name="Developed By xi.5 & sw.3", url="https://www.twitch.tv/help"))


def randnum(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


@tecno.event
async def on_ready():
    print("")
    print(f"Connected to {tecno.user}")
    print("")
    print(f"Bot ID: {tecno.user.id}")
    print("")
    print(f"Developed By xi.5 & sw.3")
    print("")
    print(f"{tecno.user} is now online.!")


allowed = ["1034102778311753899", "798245874110955520"] #Your Id here


@tecno.command()
async def p(ctx):
    global tostop
    if str(ctx.author.id) in allowed:
        tostop += 1
        await ctx.reply("**Stopped <a:Discordggvry4311:1071475306357067878>**")
    else:
        await ctx.reply("**What? <a:Discordggvry4312:1071475312409448558>**")


@tecno.command()
async def s(ctx):
    global tostop
    if str(ctx.author.id) in allowed:
        tostop = 0
        await ctx.reply("*Started <a:Discordggvry4315:1071475330587557948>*")
        while tostop == 0:
            await ctx.send(randnum('scraped.txt'))
            time.sleep(11)
    else:
        await ctx.send("**What? <a:Discordggvry4312:1071475312409448558>**")


tecno.run("Yourtoken") #tecno.run(TOKEN)
keep_alive.keep_alive()
