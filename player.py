import discord
from discord.ext import commands
import asyncio
import logging
import os

intents = discord.Intents.default()
intents.voice_states = True

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all(
), application_id=int(1102698066869485692))

@bot.event
async def on_ready():
    print("*🔈 PAREDÃO TOCANDO NO 12 🔈*")


@bot.command()
# @commands.is_owner()
async def sync(ctx, guild=None):
    if guild == None:
        await bot.tree.sync()
    else:
        await bot.tree.sync(guild=discord.Object(id=int(guild)))
    await ctx.send("**PRONTO PRA TOCAR NO 12 🔈**")


@bot.command()
# @commands.is_owner()
async def play(ctx, guild=None):
   # Verifica se o autor da mensagem está em um canal de voz
    if ctx.message.author.voice is None:
        await ctx.send("Você precisa estar em um canal de voz para executar este comando.")
        return

    # Obtém o canal de voz do autor da mensagem
    channel = ctx.message.author.voice.channel

    # Conecta ao canal de voz
    vc = await channel.connect()

    # Toca um áudio de teste
    vc.play(discord.FFmpegPCMAudio('audio.mp3'))

    # Aguarda o término da reprodução
    while vc.is_playing():
        await asyncio.sleep(1)

    

@bot.command()
# @commands.is_owner()
async def stop(ctx, guild=None):
   # Verifica se o bot está conectado a um canal de voz
    if ctx.voice_client is None:
        await ctx.send("O bot não está conectado a um canal de voz.")
        return

    # Desconecta do canal de voz
    await ctx.voice_client.disconnect()
    await ctx.send("O bot foi desconectado do canal de voz.")


bot.run("MTEwMjY5ODA2Njg2OTQ4NTY5Mg.GRDpe5.VuMH2SMmVoujIwBuiIYGjCMTAsmmM_WDHs_3EA")
