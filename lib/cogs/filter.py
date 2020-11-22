import discord
import random
from discord.ext import commands

#from discord.ext import commands
#from discord.ext.commands import Bot
#import os

import csv

keywords = []

with open('./lib/cogs/bad-words.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        word = str(row)
        keywords.append(word[2:(len(word)-2)])

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    # await message.channel.send('Hello dear friends! I will help ensure respectful language is used.')
    print('SATT Bot will help ensure respectful language is used.')

@client.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):
    # keywords = ["hun", "rape"]


    print(keywords)

    message_content = message.content.strip().lower()
    for offensive_word in keywords:
        if message.content.count(offensive_word) > 0:
            #await message.channel,send("{}, the terms you used could be offensive to others, so I've deleted your post to be safe.".format(message.author.mention))
            await message.author.send('👀 The terms you used could be offensive to others, so I\'ve deleted your most recent post to be safe.')
            await message.channel.purge(limit=1)
        await client.process_commands(message)
        #await message.channel.send("%s, the terms you used could be offensive to others, so I've deleted your post to be safe." % (message.author.id))
        #await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))    
        #await bot.delete_message(message)bot.run("TOKEN")
'''
@client.event
async def convert(ctx, argument):
    argument = await commands.MemberConverter
'''
client.run("TOKEN")


'''
bot = Bot(command_prefix=".")
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('SATT Bot will help ensure respectful language is used.')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

async def on_message(message):
    message_content = message.content.strip().lower()
    async for offensive_word in offensive_words:
        if any(offensive_word in message for offensive_word in offensive_words):
            await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))
            
            await bot.delete_message(message)bot.run(os.getenv("TOKEN"))

client.run("TOKEN")
'''

'''
bot = Bot(command_prefix="?")

with open("offensive-words.txt") as file: # offensive-words.txt contains one blacklisted phrase per line
    offensive_words = [offensive_word.strip().lower() for offensive_word in file.readlines()]

@bot.event
async def on_message(message):
    message_content = message.content.strip().lower()
    async for offensive_word in offensive_words:
        if any(offensive_word in message for offensive_word in offensive_words):
            await bot.send_message(message.channel, "{}, your message has been censored.".format(message.author.mention))
            
            with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
                self.TOKEN = tf.read()
            
            await bot.delete_message(message)bot.run(os.getenv(self.TOKEN))

'''
