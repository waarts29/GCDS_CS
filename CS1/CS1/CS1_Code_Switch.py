
import random

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

def print_colored_text(text, color):
    print(f"{COLORS.get(color.lower())}{text}\033[0m")

username = input("What is your name? ")
print(f"Hello {username}! The goal of the game is to guess the color of the text, NOT the word.\n")
wins = 0
rounds = 0

while True:
    text_color = random.choice(list(COLORS.keys()))
    print_color = random.choice(list(COLORS.keys()))
    print_colored_text(text_color, print_color)
    user_color = input("What COLOR is the text? Type 'no' to stop: ").strip().lower()
    
    if user_color == "":
        user_color = "white"

    if user_color == print_color:
        wins += 1
        print("You got it RIGHT!")
    else:
        print(f"Wrong! The color was {print_color}.")
    rounds += 1

    while True:
        print(f"Score: {wins} wins out of {rounds} games")
        again = input("Do you want to play again? Type yes or no: ").strip().lower()

        if again in ("yes", "y"):
            print()   
            break     
        elif again in ("no", "n"):
            print("Thanks for playing!")
            exit()    
        else:
            print("Please type yes or no.")


  
        
        




        
