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
player2 = "O"
step 12. grid print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]} ")
print("-----------")
print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]} ")
print("-----------")
print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]} ")
'''''
import random 


def display_board(board):
    for i in range(len(board)):
        print(" " + " | ".join(board[i]) + " ")
        if i < len(board) - 1:
            print("───┼───┼───")

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

display_board(game_board)
input()



def get_player_move(board, mark):
    while True:
        move = input(f"Player {mark}, enter row and column (e.g. 1 2): ").split()
        if len(move) != 2 or not all(m.isdigit() for m in move):
            print("Invalid input. Please enter two numbers separated by a space.")
            continue



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
        
        



