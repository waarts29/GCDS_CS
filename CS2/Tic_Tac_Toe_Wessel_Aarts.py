#PLAN WORK, WORK PLAN 
''''
step 1. create a 3x3 grid 2 dimensional
step 2. two players(human)
step 3. who goes first?
step 4. x and o?
step 5. ask user what box to choose, row column or 1,9 
step 6. after each step check who has won, diagonal, vertical, horizontal 3 in a row.
step 7. if grid {0}{0} == "x" and if {0}(1) and (0)(2) make function check win. 
step 8. if x goes 9 time and no win ganme = tie
step 9. would you liek to play again, if o break if yes reset also say who won each time keep score.
step 10. create grid grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

step 11. player1 = "X"

'''''
import random


random_shuffles = [ "player1", "player2"]


def display_board(board):
    for i in range(len(board)):
        print(" " + " | ".join(board[i]) + " ")
        if i < len(board) - 1:
            print("───┼───┼───")

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

display_board(game_board)
input()


j


def check_winner(board,mark):
    

    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    if board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    if board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True

    
    if board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    if board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    if board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True

    
    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    

    return False




def choose_first():
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    first = random.choice([player1, player2])
    if first == player1:
        second = player2
    else:
        second = player1
    print(f"{first} goes first!")

    while True:
        mark = input(f"{first}, do you want X or O? ").upper()
        if mark in ["X", "O"]:
            break
        print("Type X or O")

    if mark == "X":
        other_mark = "O"
    else:
        other_mark = "X"
    print(f"{first} is {mark}, {second} is {other_mark}")

    return first, mark, second, other_mark


def tie_checker(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True
        


