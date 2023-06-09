from asyncore import loop
import random
import time
import os
import discord
import keep_alive
from discord.ext import commands


tostop = 0

intents = discord.Intents.all()

Max = os.environ["Max"]
tecno = commands.Bot(command_prefix=".", intents=intents)


@tecno.event
async def on_connect():
    await tecno.change_presence(activity=discord.Streaming(name="Verona.?", url="https://www.twitch.tv/vveronaaaa"))


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
    print(f"Made By MAX.#0004")
    print("")
    print(f"{tecno.user} is now online.!")


allowed = ["id owner 1", "id owner 2"]


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
            await ctx.send(randnum('PFP.txt'))
            time.sleep(11)
    else:
        await ctx.send("**What? <a:Discordggvry4312:1071475312409448558>**")


tecno.run(Max) #create secret called Max
keep_alive.keep_alive()
