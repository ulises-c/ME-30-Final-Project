import random
from trivia_q_a import trivia_dictionary

def trivia():
    random_q = random.choice(list(trivia_dictionary))
    random_a = trivia_dictionary[random_q]
    response = ''

    # print(random_q)
    # response = input(random_q + ": ")
    
    if(response.lower() == trivia_dictionary.get(random_q).lower()):
        print("Correct: '{}'".format(response.capitalize()))
        
    else:
        # print("Incorrect: {}".format(trivia_dictionary.get(random_q)))
        pass
    return random_q, random_a

# test_q, test_a = trivia()
# print(test_q, test_a)