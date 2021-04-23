from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('.t'):
        await message.channel.send('No trivia questions ready yet.')

client.run(bot_token)