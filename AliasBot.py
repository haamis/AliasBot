#!/usr/bin/python3

import discord
import json
from random import *
from discord.ext import commands
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
#@asyncio.coroutine
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
#@asyncio.coroutine
async def on_message(message):
	if message.content.startswith("!alias"):
		messagelines = message.content.split("\n")
		splitmessage = messagelines[0].split(" ")
		#splitmessage = message.content.split(" ")
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
	elif message.content.startswith("!nerds"):
		splitmessage = message.content.split(" ")
		if (len(splitmessage) < 6):
			await client.send_message(message.channel, "Arguments seperated by spaces:\nnumber of dice per stat\nsize of dice\nvalue to add to roll\ncomplement\ntimes to repeat")
		else:
			messagestring = "Stats:\n"
			stats = []
			complementstats = []
			for i in range(int(splitmessage[5])):
				stat = 0
				for i in range(int(splitmessage[1])):
					stat += randint(1,int(splitmessage[2])) + int(splitmessage[3])
				stats.append(stat)
			for value in stats:
				complementstats.append(int(splitmessage[4])-value)
			stats.extend(complementstats)
			stats.sort(reverse=True)
			for value in stats:
				messagestring += str(value) + '\n'
			await client.send_message(message.channel, messagestring)
	else:
		for line in aliases[message.content]:
			await client.send_message(message.channel, line)

client.run(token)
