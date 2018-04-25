import discord
from discord.utils import get
from discord.ext.commands import Bot
from discord.ext import commands
from discord import server
import asyncio
import time

Client = discord.Client()
dlient = commands.Bot(command_prefix="!-")

@dlient.event
async def on_ready():
    print("Bot is loaded and ready.")
    print("------------------------")
    print('Logged in as ' + dlient.user.name + ' (ID:' + dlient.user.id + ') | Connected to ' + str(len(dlient.servers)) + ' servers | Connected to ' + str(len(set(dlient.get_all_members()))) + ' users')
    print('Use this link to invite {}:'.format(dlient.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(dlient.user.id))
    print("------------------------")
    print("Current version is 1.0")
    #^from the makers of BasicBot
    await dlient.change_presence(game=discord.Game(name='Spamming yo mamma too.'), status=discord.Status("dnd"))


@dlient.event #Change after message.content.strip().lower() for command name. DO NOT CHANGE AFTER THE "or" statement.
async def on_message(message):
    if message.content.strip().lower() == "spam_usr" or message.content == "Spamming once more":
        x = 1
        user = str(input("\nUser_id:\n"))
        msg = str(input("\nMessage:\n"))
        msgnumber = int(input("\nHow many messages?\n"))
        for i in range(msgnumber):
            await dlient.send_message(discord.User(id=user), msg)
        answer = str(input("\nWould you like sum more? [Y]es, [N]o:\n"))
        if answer.strip().lower() == "y":
            await dlient.send_message(dlient.get_channel("436246329090506773"), "Spamming once more")
            print("Found channel. Message sent. #%s" % x)
        if answer.strip().lower() == "n":
            print("Closing if statement.")
            return
        x += x

dlient.run("NDM3Mjc2ODQwNzE0MDQzNDAy.DbztWg.SEkEcBP56UdERPidfUecnN0-2s4")
