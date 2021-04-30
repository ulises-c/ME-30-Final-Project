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
    TriviaQnA("What is the capital of California?", "Sacramento", category="Geography", hints="North of San Francisco"),
    TriviaQnA("How many continents are there?", "7", category="Geography", hints="Odd number"),
    TriviaQnA("What is the smallest country?", "Vatican City", category="Geography", hints="The Pope"),
    TriviaQnA("What is the longest river in the world?", "Nile", category="Geography", hints="Egypt"),
    TriviaQnA("What country has the longest total coastline?", "Canada", category="Geography", hints="Maple Leaf"),
    TriviaQnA("What year was SJSU founded", "1857", category="Founding Years", hints="1800s"),
    TriviaQnA("What year was the Declaration of Independence signed?", "1776", category="Founding Years", hints="1700s"),
    TriviaQnA("What year did humans first land on the Moon?", "1969", category="Founding Years", hints="1960s"),
    TriviaQnA("What year did the US acquire the Louisiana Purchase?", "1803", category="Founding Years", hints="1800s"),
    TriviaQnA("What year was the Magna Carta signed?", "1215", category="Founding Years", hints="1200s"),
    TriviaQnA("What is the element 'Fe'", "Iron", category="Elements", hints="Starts with I"),
    TriviaQnA("What is the element 'Au'", "Gold", category="Elements", hints="Starts with G"),
    TriviaQnA("What is the element 'Ag'", "Silver", category="Elements", hints="Starts with S"),
    TriviaQnA("What is the element 'He'", "Helium", category="Elements", hints="Balloons"),
    TriviaQnA("What is the element 'Cu'", "Copper", category="Elements", hints="Pennies"),
    TriviaQnA("What is the largest organ in the human body?", "Skin", category="Human Body", hints="On the outside"),
    TriviaQnA("What is the longest bone in the human body?", "Femur", category="Human Body", hints="Leg"),
    TriviaQnA("Which grow faster fingernails or toenails?", "Fingernails", category="Human Body", hints="Holding"),
    TriviaQnA("What organ produces insulin?", "Pancreas", category="Human Body", hints="Starts with pan"),
    TriviaQnA("How many blood types are there?", "8", category="Human Body", hints="Each letter has + and -"),
    TriviaQnA("Who invented basketball?", "James Naismith", category="Inventors", hints="First name James"),
    TriviaQnA("Who invented Monopoly?", "Elizabeth Magie", category="Inventors", hints="First name Elizabeth"),
    TriviaQnA("Who invented the windshield wiper?", "Mary Anderson", category="Inventors", hints="First name Mary"),
    TriviaQnA("Who invented Hot Cheetos?", "Richard Montanez", category="Inventors", hints="First name Richard"),
    TriviaQnA("Who invented the ice cream maker?", "Nancy Johnson", category="Inventors", hints="First name Nancy"),
]

# for t in trivia_list:
#     print(t)