from discord import channel, message
import trivia_q_a
import trivia_q_a_v2
import random

# Pass these as parameters for the trivia game
trivia_questions = trivia_q_a.trivia_dictionary
trivia_questions2 = trivia_q_a_v2.trivia_list

class TriviaGame:
    def __init__(self, client, message = None, questions_list = None, hint_time=10) -> None:
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
    
    def select_question(self):
        """ Method to choose a question from the list """
        random_num = random.randint(0, len(trivia_questions2)-1)
        self.current_question = trivia_questions2[random_num].question
        self.current_answer = trivia_questions2[random_num].answers

    def get_question(self):
        return self.current_question

    def get_answer(self):
        return self.current_answer

    async def ask_question(self, msg):
        """ Method to send a question """
        self.started = True
        self.select_question()
        question = self.current_question
        self.quiz_channel = msg.channel

        await self.quiz_channel.send(question)
        await self.quiz_channel.send("For testing purposes, the answser is `{}`".format(self.current_answer))
        pass

    async def check_answer(self, msg):
        """ Method to check if a response is correct or not """
        case_insensitive_msg = msg.content.lower()
        case_insensitive_answer = self.current_answer.lower()

        if case_insensitive_msg == case_insensitive_answer:
            await msg.add_reaction('😀')
            await self.quiz_channel.send("Correct! `{}`".format(self.current_answer))
        pass

    def give_hint(self):
        """ Method to give a hint """
        pass
    
    def get_scores(self):
        return self.scores