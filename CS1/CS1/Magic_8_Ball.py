import random                                                          # load random number generator

answers = ("yes" , "no" , "maybe" , "ask again later",)                # create a list of possible answers

while True:                                                            # create a loop
    question = input("ask a question any yes or no question")          # prompts user to ask a yes or no question

    if '?' in question:                                                # check if the user put a question mark in answer
        random_answers = random.choice(answers)                        #randomly choose on of the options from answers
        print(random_answers)                                          # then print outcome
    else:                                                              # otherwise
        print("please ask a question include a ?")                     # if didnt put qoeustion mark prints in terminal please include a question mark



