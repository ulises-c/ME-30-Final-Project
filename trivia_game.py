from discord import channel, message
from trivia_q_a_v2 import trivia_list
import random
from participantv2 import participants
import time

# Pass these as parameters for the trivia game
trivia_questions2 = trivia_list

class TriviaGame:
    def __init__(self, client, message = None, questions_list = trivia_list, hint_time=5, max_points=5) -> None:
        self.client = client
        self.message = message
        self.hint_time = hint_time
        self.questions = questions_list
        self.hint_time = hint_time
        self.current_scores = []
        self.current_question = None
        self.current_answer = None
        self.current_hint = None
        self.started = False
        self.quiz_channel = None
        self.max_points = max_points 
        self.correct_answer = False

    def reset_question_answer(self):
        self.current_question = None
        self.current_answer = None
    
    def select_question(self):
        """ Method to choose a question from the list """
        random_num = random.randint(0, len(trivia_questions2)-1)
        self.current_question = self.questions[random_num].question
        self.current_answer = self.questions[random_num].answers
        self.current_hint = self.questions[random_num].hints
        print(self.questions[random_num])

    def get_question(self):
        return self.current_question

    def get_answer(self):
        return self.current_answer

    def add_participant(self, participant):
        """ This method may be used as a long term solution to a participants database """
        self.current_scores.append(participant)

    async def ask_question(self, msg):
        """ Method to send a question """
        self.started = True
        self.correct_answer = False
        self.select_question()
        question = self.current_question
        self.quiz_channel = msg.channel

        await self.quiz_channel.send(question)
        await self.quiz_channel.send("For testing purposes, the answser is `{}`".format(self.current_answer))

    async def check_answer(self, msg):
        """ Method to check if a response is correct or not """
        if self.current_answer is not None:
            case_insensitive_answer = self.current_answer.lower()
            case_insensitive_msg = msg.content.lower()

            if case_insensitive_msg == case_insensitive_answer:
                self.correct_answer = True
                await msg.add_reaction('😀')
                await msg.reply("Correct! `{0}` \n`{1}` got the point!".format(self.current_answer, msg.author))
                self.reset_question_answer()
                if(msg.author not in participants):
                    participants[msg.author] = 1
                elif(msg.author in participants):
                    participants[msg.author] += 1
                    if participants[msg.author] == self.max_points:
                        await msg.reply('Congratulations! `{0}` won the game!'.format(msg.author))
                        self.reset_scores()

    async def give_hint(self, msg):
        """ Method to give a hint after a certain amount of time passes
        Current works, but can be improved to remove the delay """
        if(self.quiz_channel == None):
            return
        keep_going = True
        start_time = time.time()
        while(keep_going):
            current_time = time.time()
            if(current_time - start_time >= self.hint_time) or (self.correct_answer):
                keep_going = False
        if(not self.correct_answer):
            await self.quiz_channel.send("Hint: {}".format(self.current_hint))    

    def quiz_end(self):
        """ End the quiz either after a certain amount of time passes without an answer/reply, or after a command to end the quiz"""
        pass
    
    async def send_scores(self, msg):
        """ Sends the current points each participant has """
        scores_string = ""
        if len(participants) < 1:
            return
        else:
            for key in participants:
                scores_string += "{}: {}\n".format(key, participants[key])
            await self.quiz_channel.send("```--- Points ---\n{}```".format(scores_string))

    async def commands_list(self, msg):
        """ Sends a list of commands """
        command_list = ["`.t` or `.trivia` to start trivia ","`.p` or `.points` to check points","`.h` or `.help` for help", "`.r` or `.reset` to reset scores"]
        await msg.reply("Commands: \n{0} \n{1} \n{2} \n{3}".format(command_list[0],command_list[1],command_list[2],command_list[3]))

    def reset_scores(self):
        for key in participants:
            participants[key] = 0
    
    async def score_reset(self, msg):
        self.reset_scores()
        await msg.reply("Cleared scores")
        