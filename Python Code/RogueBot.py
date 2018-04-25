import discord
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands
from discord import server
import asyncio
import time

Client = discord.Client()
dlient = commands.Bot(command_prefix="!")


#When it's ready it executes all of this.
@dlient.event
async def on_ready():
    print("Bot is loaded and ready.")
    print("------------------------")
    print('Logged in as ' + dlient.user.name + ' (ID:' + dlient.user.id + ') | Connected to ' + str(len(dlient.servers)) + ' servers | Connected to ' + str(len(set(dlient.get_all_members()))) + ' users')
    print('Use this link to invite {}:'.format(dlient.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(dlient.user.id))
    await dlient.change_presence(game=discord.Game(name='Intense PyCharm'), status=discord.Status("dnd"))

#Does things when a member gets banned.
@dlient.event
async def on_member_ban(member):
    for x in dlient.get_all_emojis():
        if x.id == '436279787237933067':
            return x
    await dlient.send_message(dlient.get_channel("435033746794741760"), "%s has just been hit with the %s :hammer: ."% (member, x))

@dlient.event
async def on_member_unban(member):
    for x in dlient.get_all_emojis():
        if x.id == '436279787237933067':
            return x
    await dlient.send_message(dlient.get_channel("435033746794741760"), "%s has returned from the dead!" % member)


#The first reaction I made and .content code and shit like that.
@dlient.event
async def on_message(message):

    #checks if the message is from the actual bot.
    if message.author == dlient.user:
        return

    #Get :ban emoji:
    for x in dlient.get_all_emojis():
        if x.id == '436279787237933067':
            return x


    if "one of us" in message.content:
        await dlient.send_message(message.channel, 'One of us.')

    if "One of us" in message.content:
        await dlient.send_message(message.channel, 'One of us.')

    #Simulate a ban
    if message.content == "simulate":
        await dlient.send_message(message.channel, "%s has just been hit with the %s :hammer: ."% (message.author.mention, x))

    if "nice" in message.content:
        await dlient.add_reaction(message, "🇳")
        await dlient.add_reaction(message, "🇮")
        await dlient.add_reaction(message, "🇨")
        await dlient.add_reaction(message, "🇪")

    if "NICE" in message.content:
        await dlient.add_reaction(message, "🇳")
        await dlient.add_reaction(message, "🇮")
        await dlient.add_reaction(message, "🇨")
        await dlient.add_reaction(message, "🇪")

    if "Nice" in message.content:
        await dlient.add_reaction(message, "🇳")
        await dlient.add_reaction(message, "🇮")
        await dlient.add_reaction(message, "🇨")
        await dlient.add_reaction(message, "🇪")

    if "very" in message.content:
        await dlient.add_reaction(message, x)

dlient.run("NDM1NTM5Nzk1ODY3ODYxMDIy.DbeqrQ.9YjjmyuAix8alZJOdmlA3I9L3rA")
