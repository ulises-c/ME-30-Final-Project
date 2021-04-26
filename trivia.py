import random
from trivia_q_a import trivia_dictionary

def trivia():
    random_q = random.choice(list(trivia_dictionary))
    response = ''
    # response = input(random_q + ": ")
    
    if(response.lower() == trivia_dictionary.get(random_q).lower()):
        print("Correct: '{}'".format(response.capitalize()))
    else:
        print("Incorrect: {}".format(trivia_dictionary.get(random_q)))
    return random_q

trivia()