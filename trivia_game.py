from discord import channel, message
from trivia_q_a_v2 import trivia_list
import random
from participantv2 import participants

# Pass these as parameters for the trivia game
trivia_questions2 = trivia_list

class TriviaGame:
    def __init__(self, client, message = None, questions_list = trivia_list, hint_time=10) -> None:
        self.client = client
        self.message = message
        self.hint_time = hint_time
        self.questions = questions_list
        self.hint_time = hint_time
        self.current_scores = []
        self.current_question = None
        self.current_answer = None
        self.started = False
        self.quiz_channel = None

    def reset_question_answer(self):
        self.current_question = None
        self.current_answer = None
    
    def select_question(self):
        """ Method to choose a question from the list """
        random_num = random.randint(0, len(trivia_questions2)-1)
        self.current_question = self.questions[random_num].question
        self.current_answer = self.questions[random_num].answers
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
                await msg.add_reaction('😀')
                # await self.quiz_channel.send("Correct! `{}`".format(self.current_answer))
                await msg.reply("Correct! `{}`".format(self.current_answer))
                self.reset_question_answer()
                if(msg.author not in participants):
                    participants[msg.author] = 1
                elif(msg.author in participants):
                    participants[msg.author] += 1

    def give_hint(self):
        """ Method to give a hint after a certain amount of time passes """
        pass

    def quiz_end(self):
        """ End the quiz either after a certain amount of time passes without an answer/reply, or after a command to end the quiz"""
        pass
    
    async def send_scores(self, msg):
        scores_string = ""
        if len(participants) < 1:
            return
        else:
            for key in participants:
                scores_string += "{}: {}\n".format(key, participants[key])
            await self.quiz_channel.send("```--- Points ---\n{}```".format(scores_string))