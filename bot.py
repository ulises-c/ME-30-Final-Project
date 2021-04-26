# Used to log in the bot and have the token hidden
from dotenv import load_dotenv
import os
load_dotenv()
bot_token = os.getenv('secret_bot_token')

# Library to use the discord api for python
import discord
from discord.ext import commands

# Files created for this project
import trivia
import Participant

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    # print(message.author)
    if message.author == client.user:
        return
    
    if message.content.startswith('.t'):
        # await message.channel.send('No trivia questions ready yet.')
        trivia_q = trivia.trivia()
        await message.channel.send(trivia_q)
        await message.add_reaction('🙂')

client.run(bot_token)