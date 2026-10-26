# ! código base
import random

import discord
from discord.ext import commands

from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

# ! Código base acima

## opcionais

# Lista de dicas de sustentabilidade
dicas = [
    "Use uma garrafa reutilizável!",
    "Separe os materiais recicláveis!",
    "Apague as luzes ao sair do cômodo!",
    "Evite desperdício de água!",
    "Reutilize potes e embalagens!",
]


#! código base
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.command()
async def hello(ctx):
    mensagem = (
        "🌎 **Olá! Eu sou o EcoBot!**\n"
        "Vamos cuidar do meio ambiente juntos!\n\n"
        "**Escolha uma opção:**\n"
        "`$dica` - Receba uma dica sustentável.\n"
        "`$dicas` - Veja todas as dicas.\n"
        "`$desafio` - Receba um desafio ecológico.\n"
        "`$ajuda` - Veja os comandos disponíveis."
    )

    await ctx.send(mensagem)


@bot.command()
async def dica(ctx):
    await ctx.send(random.choice(dicas))


@bot.command()
async def dicas(ctx):
    mensagem = "\n".join(f"🌱 {dica}" for dica in dicas_lista())
    await ctx.send(mensagem)


def dicas_lista():
    return dicas


@bot.command()
async def desafio(ctx):
    desafios = [
        "Passe um dia sem usar copos descartáveis!",
        "Separe os recicláveis da sua casa!",
        "Evite deixar a torneira aberta sem necessidade!",
        "Reutilize algum objeto antes de descartá-lo!",
    ]

    await ctx.send("🌿 Seu desafio: " + random.choice(desafios))


@bot.command()
async def ajuda(ctx):
    await ctx.send(
        "Comandos disponíveis: `$hello`, `$dica`, " "`$dicas`, `$desafio` e `$ajuda`."
    )


#! rodar o bot

bot.run(TOKEN)
