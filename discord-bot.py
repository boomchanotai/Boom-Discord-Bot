import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready() :
    print(f"Logged in as {client.user}")

@client.event
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
        # for image in imageList:
        #     if image.find(".DS_Store") == 0:
        #         continue
        #     else :
        #         print(image)
    elif message.content == "ขอซีมอสทรงแหลม" :
        await message.channel.send(file=discord.File("images/image4.jpeg"))
    elif message.content == "ขอไปโดยตึกตายไป" :
        await message.channel.send(file=discord.File("images/IMG_1174.jpg"))

client.run(os.getenv('TOKEN'))