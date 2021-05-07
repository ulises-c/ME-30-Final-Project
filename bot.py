# Library to use the discord api for python
import discord
from discord.ext import commands

# Files created for this project
import trivia_game as tg

# Used to load token to login to the Discord Bot
from env_token import local_token
from env_token import heroku_token

client = commands.Bot(command_prefix='.')
trivia = tg.TriviaGame(client)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('.t') or message.content == ('.trivia'):
        await trivia.ask_question(message)
        await trivia.give_hint(message)
        
    elif not message.content == ('.t') or not message.content == ('.trivia') and trivia.started:
        await trivia.check_answer(message)
    
    if message.content == ('.p') or message.content == ('.points'):
        await trivia.send_scores(message)
    
    if message.content == ('.h') or message.content == ('.help'):
        await trivia.commands_list(message)

    if message.content == ('.r') or message.content == ('.reset'):
        await trivia.reset_message(message)

    if message.content == ('.g') or message.content == ('.github'):
        await trivia.send_github(message)
    
    if message.content == ('.e') or message.content == ('.end'):
        await trivia.force_end(message)

# client.run(local_token)
client.run(heroku_token)