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

def updateAliases():
	with open("aliases",'w') as fh:
		json.dump(aliases, fh)

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
			updateAliases()
			yield from client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " added.")
		if splitmessage[1] == "remove":
			aliases.pop(splitmessage[2])
			updateAliases()
			yield from client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " removed.")
		if splitmessage[1] == "list":
			alias_list = ""
			for a in aliases:
				alias_list += a + " : " + aliases[a] + "\n"
			yield from client.send_message(message.channel, message.author.mention + "\n" + alias_list)
	else:
		yield from client.send_message(message.channel, aliases[message.content])

client.run('MzYwMTQwOTcxODM4NTM3NzI4.DKRPBw.CBYJlnbK4bzJ5jeHXbt783-XaIk')
