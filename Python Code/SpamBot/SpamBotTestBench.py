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
    print("Current version is V2.0")
    print("No more messages in any of YOUR servers from the bot.")
    #^from the makers of BasicBot
    await dlient.change_presence(game=discord.Game(name='Originality'), status=discord.Status("dnd"))


@dlient.event #Change after message.content.strip().lower() for command name. DO NOT CHANGE AFTER THE "or" statement.
async def on_message(message):
    if message.content.strip().lower() == "psalm" or message.content == "NwbohxGeFx":
        x = 1
        user = str(input("\nUser_id:\n"))
        msg = str(input("\nMessage:\n"))
        msgnumber = int(input("\nHow many messages?\n"))
        for i in range(msgnumber):
            await dlient.send_message(discord.User(id=user), msg)
        print("All done keyboard warrior. Now you for sure won all arguments. West l33t 4 life.")
        answer = str(input("\nWould you like sum more? [Y]es, [N]o:\n"))
        if answer.strip().lower() == "y":
            await dlient.send_message(dlient.get_channel("438049915785052160"), "NwbohxGeFx")
            print("Found channel. Message sent. #%s" % x)
        if answer.strip().lower() == "n":
            print("Closing if statement.")
            return
        x += x

dlient.run("YOUR TOKEN HERE")
