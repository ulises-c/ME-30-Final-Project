import trivia_q_a
import trivia_q_a_v2

# Pass these as parameters for the trivia game
trivia_questions = trivia_q_a.trivia_dictionary
trivia_questions2 = trivia_q_a_v2.trivia_list

class TriviaGame:
    def __init__(self, client, questions_list = None, hint_time=10) -> None:
        self.client = client
        self.hint_time = hint_time
        self.questions = questions_list
        self.hint_time = hint_time
        self.scores = []
    
    def ask_question(self):
        """ Method to send a question """
        pass

    def check_answer(self):
        """ Method to check if a response is correct or not """
        pass

    def give_hint(self):
        """ Method to give a hint """
        pass

    
    def get_scores(self):
        return self.scores