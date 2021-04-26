"""
A different method of approaching the trivia Q&A list.
Instead of using a dictionary, create a list of objects
"""

class TriviaQnA:
    def __init__(self, question, answers, category = None, hints = None) -> None:
        self.question = question
        self.answers = answers
        self.category = category
        self.hints = hints

    def get_hint(self):
        return self.hints

    def __str__(self) -> str:
        the_string = "\nQ:'{}' \nA:'{}' \nCategory: '{}' \nHint(s):'{}'".format(self.question, self.answers, self.category, self.hints)
        return the_string

# List of trivia questions
trivia_list = [
    TriviaQnA("What is the capital of California?", "Sacramento", category="Geography"),
    TriviaQnA("What year was SJSU founded", "1857", hints="1800s")
]

# for t in trivia_list:
#     print(t)