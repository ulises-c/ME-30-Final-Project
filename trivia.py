import random
from trivia_q_a import trivia_dictionary

def trivia():
    random_q = random.choice(list(trivia_dictionary))
    response = input(random_q + ": ")
    if(response == trivia_dictionary.get(random_q)):
        print("Correct: '{}'".format(response))
    else:
        print("Incorrect: {}".format(trivia_dictionary.get(random_q)))

trivia()