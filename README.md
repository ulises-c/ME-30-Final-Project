# ME-30-Final-Project
 - SJSU ME 30 Final Project Spring 2021
 - A trivia bot for discord
 
 ## How the game will work
 - To start the game send a trigger phrase like `.trivia` to activate the bot
 - The bot will send a random trivia question from a dictionary
 - The bot will wait up to 20 seconds for someone to send the correct answer
 - The first person to submit the correct answer gets awarded a point
 - If no one answers then the bot deactivates



## Roadmap
#### Completed
- Have a bot that connects to discord
- Create a trivia game that works in the terminal
- Have the discord bot send trivia questions with a trigger phrase
- Have the bot recognize correct answers
- Have the bot add a reaction emoji ONLY to the first person to respond with the correct answer
- Add a point system
- Add a method that sends a list of commands
- Add a method to reset scores with a command
- Add a hint system (Need improvement, currently stalls other processes)
- Host the bot online on a server instead of a local host (Hosted via Heroku)
#### In Progress
- Add a method to automatically send a new question after a question is correctly answered
- Add a method for the scores list to reset after a certain amount of time of inactivity
- Add a method so the an ongoing trivia game is only done in one channel
- Add more questions
- Create a database to keep track of points
