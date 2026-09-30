#cat
import random                                                                                               #imports random number generator
import getpass                                                                                              # imports a passowrd thing into terminal so other user can see what you type

player_score = 0                                                                                            # set player scores to 0
computer_score = 0                                                                                          # set computer score to 0
player2_score = 0                                                                                           # set player score to 0
random_choices = ["rock", "paper", "scissors"]                                                              # random machines choices are either rock paper or scissors

mode = input("Do you want to play against machine or another user? ").lower()                               # set to either play against  other user or another player

if mode not in ["machine", "user"]:                                                                         # but if user doesnt pck eithe ruser or machine
    print("Invalid mode. Please restart and type 'machine' or 'user'.")                                     # then says restart if typed wrong
    exit()                                                                                                  # then restart

while True:                                                                                                 # loop
    if mode == "machine":                                                                                   # if the mode is typed as machine
        random_choice = random.choice(random_choices)                                                       # if the computers choice make it random and define it as the machines choice
        user_choice = input("Choose rock, paper, or scissors: ").lower()                                    # if the user choice equals one f the three keep it to one so that it doesnt do all three arguments at the same time

        if user_choice == random_choice:                                                                    # if the user choice is the same as random choice
            print("You and the machine picked the same choice, try again")                                  # then prints in terminal that thye picked the same choice 
            continue                                                                                        # go back to top of loop
        elif user_choice == "rock" and random_choice == "paper":                                            # otherewsie if user is rock and comuter is paper then 
            print("Machine won, try again")                                                                 # print mchine won
            computer_score += 1                                                                             # then add to computer score
        elif user_choice == "paper" and random_choice == "scissors":                                        # otherwise if user choic eis paper and machine choice s scissors
            print("Machine won, try again")                                                                 # then terminal prints machine won
            computer_score += 1                                                                             # then add one to computer score
        elif user_choice == "scissors" and random_choice == "rock":                                         # if user is scissors and machine is rock then print machine won
            print("Machine won, try again")                                                                 # the print machine won
            computer_score +=1                                                                              # add to computer score
        elif user_choice == "rock" and random_choice == "scissors":                                         # if user choice is rock and random choice is scirssors 
            print("You win!!")                                                                              # then print you win
            player_score += 1                                                                               # then add one to player score 
        elif user_choice == "paper" and random_choice == "rock":                                            # if user choice is paper and machine choice is rock then
            print("You win!!")                                                                              # print you win
            player_score += 1                                                                               # then add 1 to player score 
        elif user_choice == "scissors" and random_choice == "paper":                                        # if user choice is scissors and amchine choice is paper then
            print("You win!!!")                                                                             # print you win
            player_score += 1                                                                               # adds to user score
        else:                                                                                               # else
            print("Invalid response, please type rock, paper, or scissors.")                                # the print in terminal invalid response etc
            continue                                                                                        # then continue

        print(f"Current Score: Player - {player_score}, Computer - {computer_score}")                       # this is code for thepalyer and machine code

    elif mode == "user":                                                                                    # otherewise if the mode is user then
        player1_choice = getpass.getpass("Player 1, choose rock, paper, or scissors (hidden): ").lower()    # player 1 has a password, so when they type it doesnt show up
        player2_choice = getpass.getpass("Player 2, choose rock, paper, or scissors (hidden): ").lower()    # same for player 2

        if player1_choice == player2_choice:                                                                # if player 1 and player 2 have same choice
            print("You both picked the same choice, try again.")                                            # if player one and players two choice is equal
            continue                                                                                        # go back to top loop
        elif player1_choice == "rock" and player2_choice == "paper":                                        # if player 1 choice is rock and player 2 is paper then 
            print("Player 2 won, try again.")                                                               # print player 2 won
            player2_score += 1                                                                              # then add score to to player 2
        elif player1_choice == "paper" and player2_choice == "scissors":                                    #if playe r1 chooses paper and player 2 scisssors then
            print("Player 2 won, try again.")                                                               # player 2 wins
            player2_score += 1                                                                              # add to player 1 score
        elif player1_choice == "scissors" and player2_choice == "rock":                                     # player 1 choice is scissors and player 2 choice is rock then
            print("Player 2 won, try again.")                                                               #prints player 2 wins
            player2_score += 1                                                                              # plyaer 2 score +1
        elif player1_choice == "rock" and player2_choice == "scissors":                                     # if player 1 choice and player 2 choice  is scissors
            print("Player 1 wins!!")                                                                        # prints player 1 wins
            player_score += 1                                                                               # add to player 1 score
        elif player1_choice == "paper" and player2_choice == "rock":                                        # if player 1 choice is papaer and player 2 is rock then
            print("Player 1 wins!!")                                                                        # the prints player 1 wins
            player_score += 1                                                                               # add 1 to player 1 score 
        elif player1_choice == "scissors" and player2_choice == "paper":                                    # if player 1 choice is scissors and player 2 is paper 
            print("Player 1 wins!!")                                                                        # print player 1 wins
            player_score += 1                                                                               # add to  player 1 score
        else:                                                                                               #  otherwise 
            print("Invalid response, please type rock, paper, or scissors.")                                # if didn;t type rock paper or scissors then prints invalid response
            continue                                                                                        # then restart to top of while true

        print(f"Current Score: Player 1 - {player_score}, Player 2 - {player2_score}")                      # to inpit scores for player and player 2

