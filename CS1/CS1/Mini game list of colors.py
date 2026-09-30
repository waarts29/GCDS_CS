import random

colors = ["red", "blue", "orange", "yellow"]
color_choice = random.choice(colors)
tries = 0

while tries < 3: 
    user_choice = input(f"Guess out of {colors}").lower()

    if user_choice == color_choice:
        tries += 1 
        print("You win!")
        break
    else: 
        tries += 1
        print(f"You missed you have {2 - tries} remaining. ") 

     




