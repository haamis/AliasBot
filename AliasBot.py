#!/usr/bin/python3

import discord
import json
#from discord.ext import commands
import asyncio

client = discord.Client()

aliases = {}

token = ""

with open("aliases") as fh:
	aliases = json.load(fh)

with open("token") as fh:
	token = fh.read().strip('\n')

def updateAliases():
	with open("aliases",'w') as fh:
		json.dump(aliases, fh)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith("!alias"):
		messagelines = message.content.split("\n")
		splitmessage = messagelines[0].split(" ")
		if splitmessage[1] == "add":
			aliases[splitmessage[2]] = messagelines[1:]
			updateAliases()
			await client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " added.")
		elif splitmessage[1] == "remove":
			aliases.pop(splitmessage[2])
			updateAliases()
			await client.send_message(message.channel, message.author.mention + " Alias " + splitmessage[2] + " removed.")
		elif splitmessage[1] == "list":
			alias_list = ""
			for a in aliases:
				alias_list += a + " : " + '\n'.join(aliases[a]) + "\n"
			await client.send_message(message.channel, message.author.mention + "\n" + "```" + alias_list + "```")
	else:
		try:
			for line in aliases[message.content]:
				await client.send_message(message.channel, line)
		except KeyError:
			pass

client.run(token)