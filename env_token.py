""" Used to log in the bot and have the token hidden """ 
from dotenv import load_dotenv
import os
load_dotenv('.env')
local_token = os.getenv('secret_bot_token') # Use when testing locally

class Config(object):
    OAUTH_TOKEN = os.getenv('OAUTH_TOKEN') 