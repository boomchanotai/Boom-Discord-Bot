import discord
import random
import os
from dotenv import load_dotenv

from discord.ext import commands


from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

import pafy

load_dotenv()

# client = discord.Client()

bot = commands.Bot(command_prefix="$", help_command=None)

@bot.event
async def on_ready() :
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.content == "Tui is gay":
        for i in range(5):
            myid = '<@567875441596039179>'
            await message.channel.send(f"{myid} is gay !")
        # for i in range(5):
        #     await message.channel.send("Hello World !")
    elif message.content == "Tui nahee":
        for i in range(5):
            myid = '<@856791404302172170>'
            await message.channel.send(f"{myid} Nahee !")
    elif message.content == "Boombotcheck":
        id = message.author.id
        await message.channel.send(f"Kuy rai <@{id}> !")
    elif message.content == "ตุ้ยชอบใคร":
        tui = ["ณิชา","แท่นแท้น","พี่แป้ง","บีเอม","โบวลิ่ง","ผิงผิง","จารย์ฝ้าย","วาวา","แพนเค้ก","นัน","ไนท์"]
        await message.channel.send("ตุ้ยชอบ"+ random.choice(tui))
    elif message.content == "สุ่มมีม":
        imageList = os.listdir("images")
        imageList.remove(".DS_Store")
        await message.channel.send(file=discord.File("images/" + random.choice(imageList)))
    elif message.content == "ขอซีมอสทรงแหลม" :
        await message.channel.send(file=discord.File("images/image4.jpeg"))
    elif message.content == "ขอไปโดดตึกตายไป" :
        await message.channel.send(file=discord.File("images/IMG_1174.jpg"))

    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if not ctx.author.voice:
        await ctx.send("You are not in a voice channel")
        return
    
    if voice_client == None:
        await ctx.channel.send(f":thumbsup: Joined `{channel.name}`")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)

    VDL_OPTIONS = { 'format': 'bestaudio', 'noplaylist': 'True' }
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not voice_client.is_playing():
        await ctx.channel.send(f":musical_note: Searching :mag_right: `{url}`")
        try:
            video = pafy.new(url)
            value = video.title
            await ctx.channel.send(f"Playing :notes: `{value}` - Now!")
        except:
            await ctx.channel.send(f"Playing :notes: `มึงใส่ลิ้งค์ให้ถูกไอสัส กูจะได้หาชื่อมาแสดงได้` - Now!")
        with YoutubeDL(VDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else:
        await ctx.channel.send("Already playing !")
        return

@bot.command()
async def leave(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    await voice_client.disconnect()

@bot.command()
async def stop(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("❌❌❌ Bot isn't connected to Voice Channel !")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send(f"❌❌❌ You aren't in `{voice_client.channel.name}`")
        return
    
    voice_client.stop()

@bot.command()
async def pause(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("❌❌❌ Bot isn't connected to Voice Channel !")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send(f"❌❌❌ You aren't in `{voice_client.channel.name}`")
        return
    
    if not voice_client.is_playing():
        await ctx.channel.send(f"❌❌❌ You aren't listen to anything !")
        return
    
    voice_client.pause()

@bot.command()
async def resume(ctx):
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("❌❌❌ Bot isn't connected to Voice Channel !")
        return

    if voice_client.channel != ctx.author.voice.channel:
        await ctx.channel.send(f"❌❌❌ You aren't in `{voice_client.channel.name}`")
        return
    
    if not voice_client.is_playing():
        await ctx.channel.send(f"❌❌❌ You aren't listen to anything !")
        return
    
    voice_client.resume()

bot.run(os.getenv('TOKEN'))