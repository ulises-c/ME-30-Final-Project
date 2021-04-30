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
import trivia_game
from trivia_q_a_v2 import trivia_list

client = commands.Bot(command_prefix='.')
quiz = trivia_game.TriviaGame(client, questions_list=trivia_list)
current_a = ""

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    # print(message.author)
    if message.author == client.user:
        return

    if message.content.startswith('.t'):
        await quiz.ask_question(message)

    elif not message.content.startswith('.t') and quiz.started:
        await quiz.check_answer(message)
               
client.run(bot_token)