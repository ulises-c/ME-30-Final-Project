# Library to use the discord api for python
import discord
from discord.ext import commands

# Files created for this project
import trivia_game as tg

# Used to load token to login to the Discord Bot
from env_token import Config
from env_token import local_token

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
        # Currently creates a 10 second delay between any action after give_hint is called
        
    elif not message.content == ('.t') or not message.content == ('.trivia') and trivia.started:
        await trivia.check_answer(message)
    
    if message.content == ('.p') or message.content == ('.points'):
        await trivia.send_scores(message)
    
    if message.content == ('.h') or message.content == ('.help'):
        """ Send a list of commands """
        await trivia.commands_list(message)

    if message.content == ('.r') or message.content == ('.reset'):
        await trivia.score_reset(message)

the_token = Config['OAUTH_TOKEN']
client.run(the_token)
# client.run(local_token)