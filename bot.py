# Used to log in the bot and have the token hidden
from dotenv import load_dotenv
import os
load_dotenv()
bot_token = os.getenv('secret_bot_token')

# Library to use the discord api for python
import discord
from discord.ext import commands

# Files created for this project
import trivia_game as tg

client = commands.Bot(command_prefix='.')
trivia = tg.TriviaGame(client)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('.t' or 'trivia'):
        await trivia.ask_question(message)

    elif not message.content == ('.t' or 'trivia') and trivia.started:
        await trivia.check_answer(message)
    
    if message.content == ('.p' or 'points'):
        await trivia.send_scores(message)
    
    if message.content == ('.h' or '.help'):
        """ Send a list of commands """
        await message.reply("Still under development")
               
client.run(bot_token)