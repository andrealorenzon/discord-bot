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
    with open('bsl.txt') as f:
        bsl = f.readlines()

    if any(b in message.content for b in benvenuti):
        composed = random.sample(bsl, 10)
        await message.channel.send(f"Benvenutå su litigi, il server discord di \
riferimento per /{', '.join(composed)}")

if __name__ == "__main__":
    bot.run(TOKEN)
