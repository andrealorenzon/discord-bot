import os
from discord.ext import commands
import random
import datetime

seen = {}
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

    #log
    user_key = message.author.name.lower()
    seen[user_key] = datetime.datetime.now()

    if message.content.startswith("!seen"):
        lookup_name = message.content[6:].lower()
        lst_time = seen.get(lookup_name, None)
        if lst_time:
            timestring = seen[lookup_name].strftime("%d/%m/%Y, %H:%M")
            response = f"Ho visto {message.content[5:]} per l'ultima volta: {timestring} "
        else:
            response = "Mi spiace, non lo vedo da un po'."
        await message.channel.send(response)
                

    elif message.content == '99!':
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    elif "bottana" in message.content.lower():
        await message.channel.send("Oh sì, fammi tua. [50€]")

    elif "negro" in message.content.lower() or "negra" in message.content.lower():
        await message.channel.send("Che roba da sfigati usare negro come insulto.")

    elif 'ital' in message.content.lower().strip():
        for word in [
            "ritaly",
            "italy",
            "ritalì",
            "ritali",
            "ritalini",
            "ritalino",
            "ritalin",
            "ritali",
            "itali"
        ]:
            if word in message.content:
                await message.channel.send("OK, ma cheppalle parlare di Italy. :(")
                return

    elif 'benvenut' in message.content.lower():
        benvenuti = [f"benvenut{x} su litigi" for x in [
            'o', 'a', 'i', 'e', 'ə']]
        with open('bsl.txt') as f:
            bsl = [row.strip() for row in f.readlines()]

        if any(b in message.content for b in benvenuti):
            composed = random.sample(bsl, 10)
            complete = ', '.join(composed)
            complete.replace("?,", "?")
            await message.channel.send(f"Benvenutå su litigi, il server discord di \
    riferimento {complete}")
            return

    elif 'milano' in message.content.lower():
        await message.channel.send('''Con 367 miliardi di dollari, l'area metropolitana di Milano è la prima area in Italia e l'undicesima al mondo per prodotto interno lordo e altre supercazzole assortite su multinazionali, informatica, sistema bancario, biotecnologie, invenzioni, borsa, borsette. Questo per dire che ti stai mettendo contro un nemico potente e che veste sicuramente MaisonMargiela. Cancella quella cartellina, non costringermi a chiamare Fec(vincitore mongolino 2021) per una visura ipocatastale al tuo ano.''')

if __name__ == "__main__":
    bot.run(TOKEN)
