#!/usr/bin/python3

import discord
import json
from discord.ext import commands
import asyncio

#if not discord.opus.is_loaded():
#    discord.opus.load_opus('/usr/lib/x86_64-linux-gnu/libopus.so')

client = discord.Client()

with open("aliases") as fh:
	aliases = json.load(fh)

@client.event
@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
@asyncio.coroutine
def on_message(message):
	if message.content.startswith("!alias"):
		splitmessage = message.content.split(" ")
		if splitmessage[1] == "add":
			aliases[splitmessage[2]] = " ".join(splitmessage[3:])
			yield from client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " added.")
		if splitmessage[1] == "remove":
			aliases.pop(splitmessage[2])
			yield from client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " removed.")
	else:
		yield from client.send_message(message.channel, aliases[message.content])

client.run('MzYwMTQwOTcxODM4NTM3NzI4.DKRPBw.CBYJlnbK4bzJ5jeHXbt783-XaIk')
