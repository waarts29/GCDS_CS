import random

answers = ("yes" , "no" , "maybe" , "ask again later",)

while True:
    question = input("ask a question any yes or no question")

    if '?' in question:
        random_answers = random.choice(answers)
        print(random_answers)
    else:
        print("please ask a question include a ?")



