import discord
from discord.ext import commands
from googletrans import Translator
from googletrans import constants
import os


translator = Translator()
bot = commands.Bot(command_prefix="$")
languages = constants.LANGUAGES
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

async def on_message(message):
    if message.author == bot.user: return

@bot.command()
async def trad(ctx, *arg):
    texto = ' '.join(arg[:-2])
    traducao = translator.translate(texto, dest=arg[-1], src=arg[-2]).text
    #print(arg)
    await ctx.channel.send(f'{texto} em {languages[arg[-1]]} é {traducao}')


bot.run(DISCORD_TOKEN)