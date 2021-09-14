from re import match
import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

async def createTeam(guild, author):
    allTeams = [x for x in guild.roles if x.name.find("team") != -1]
    role = await guild.create_role(name=f"team{str(len(allTeams) + 1).zfill(2)}", colour=discord.Colour(0xF6BE00))
    await author.add_roles(role)
    return role

@bot.command()
async def get_members(ctx,role_name,channel):
    role = discord.utils.find(
        lambda r: r.name == role_name, ctx.guild.roles)
        
    members = []
    for user in ctx.guild.members:
        if role in user.roles:
            members.append(user.mention)
    
    await channel.send(f"{role.mention} | {' '.join(members)} ")

@client.event
async def on_ready() :
    print(f"Logged in as {client.user}")

@client.event
async def on_message(ctx):
    message = ctx.content
    guild = ctx.guild
    author = ctx.author
    
    if message.startswith('!team'):
        try:
            command = message.split(" ")[1]
        except:
            command = "help"
            
        if command == "add":
            if len(message.split(" ")) >= 2 :
                userTeam = [x for x in author.roles if x.name.find("team") != -1]
                if not len(userTeam) :
                    newRole = await createTeam(guild, author)

                for mention in ctx.mentions:
                    await discord.Member.add_roles(mention, userTeam[0] if len(userTeam) else newRole)
            else :
                await ctx.channel.send("You have entered wrong command. please try, !team add <user>")
        elif command == "help":
            print("Help")
        elif command == "list":
            team_list_channel = [x for x in guild.channels if x.name.find("team-list") != -1][0]

            messages = await team_list_channel.history(limit=100).flatten()

            for message in messages :
                print(message.content)

            if (messages == None) :
                role = [x for x in guild.roles if x.name.find("team") != -1]
                role.sort(key=lambda x: int(x.name[-2:]), reverse=False)
                for role in role :
                    if role.name.find("team") != -1 :
                        await get_members(ctx, role.name, team_list_channel)
            
        else:
            print('unknown')

client.run(os.getenv('UNISEC_TOKEN'))