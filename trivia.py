import random

trivia_dictionary = {
    "What is the capital of California?":"Sacramento",
    "What year was SJSU founded":"1857",
    "What is the element 'Fe'":"iron"
}

def trivia():
    random_q = random.choice(list(trivia_dictionary))
    response = input(random_q + ": ")
    if(response == trivia_dictionary.get(random_q)):
        print("Correct: '{}'".format(response))
    else:
        print("Incorrect: {}".format(trivia_dictionary.get(random_q)))

trivia()