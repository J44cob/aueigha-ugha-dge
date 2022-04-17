import asyncio
import requests
import random
import string
import discord
from discord.ext import commands
from discord.ext import tasks
import os
eth_api = "https://api.coinbase.com/v2/exchange-rates?currency=ETH"
headers = {"Accept": "application/json"}
bot = commands.Bot(command_prefix= '.')

def get_eth_price():
    r = requests.request("GET", eth_api, headers=headers)
    data2 = r.json()
    eth_price = data2['data']['rates']['USD']
    return eth_price

#-------------------------------------------------------------------------------

@bot.command()
async def eth(ctx):
    await ctx.send(f"The price of **ETH** is **{get_eth_price()}$**")

#-------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print('The bot is online')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=(f"Eth is {get_eth_price()}$")))

@tasks.loop(seconds=20.0)
async def ch_pr():
    await bot.wait_until_ready()
    while not bot.is_closed():
        channel = bot.get_channel(958080934979182713)
        await channel.send(f'>>> The price of Etherium is **{get_eth_price()}$**')
        await asyncio.sleep(20)
bot.loop.create_task(ch_pr())
bot.run("OTU3NDEzMzkzNjYzNDE0MzUy.Yj-atA.pySF5Xj_KNBEifskDvFaKDFuHv8")