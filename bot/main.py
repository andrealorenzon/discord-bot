import os
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    
    for word in [
        "italy",
        'ritaly',
        'ritalin',
        'palo e palle',
        'visura',
        'pennetta',
        'talpone',
        ]:
        if word in message.content:
            await message.channel.send("OK, ma cheppalle parlare di Italy. :(")

    benvenuti = [
        "benvenuto su litigi", 
        "benvenuta su litigi", 
        "benvenuti su litigi",  
        "benvenute su litigi", 
        "Benvenutə su litigi",
        ]
    if any(b in message.content for b in benvenuti):
        await message.channel.send("Benvenutå su litigi, il sub che ha risolto l'annoso \
problema dei pronomi e che infatti spara più stronzate procapite al mondo. Ma \
non tanto per dire, è certificato proprio, campioni di reddit, sucate tutti, \
che qui siamo competitivi mica diciamo gni gni gni bravi tutti, fiera dell'amicizia \
tra sub... l'unico sub che teniamo vicino è quello dove ci stanno le XX per \
ovvi motivi (e quello dove fappano ma zero virili strette di mano). Che poi, la figa \
piace a molti, il cazzo piace a tutti, basta vedere le statistiche. Benvenutå a \
casa grafomani, dispersi del web primi anni 00, onlyfansers e in generale chiunque \
abbia un buco del culo che lo obblighi a scrivere quand'è al cesso. *Please note: \
this public service is provided for free so don't cagacazz*")

if __name__ == "__main__":
    bot.run(TOKEN)
