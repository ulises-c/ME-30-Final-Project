import discord
from discord.ext import commands

class Participant:
    def __init__(self, message, points):
        self.user = message.author # discord api
        self.points = points

    def add_points(self):
        # based on correct answer from trivia response
        pass
    
    def __str__(self):
        return "{} has {} points".format(self.user, self.points)