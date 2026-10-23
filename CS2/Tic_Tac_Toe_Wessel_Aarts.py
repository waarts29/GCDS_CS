
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






def display_board(board):
    print (" 1   2   3")
    for i in range(len(board)):
        print(" " + " | ".join(board[i]) + " ")
        if i < len(board) - 1:
            print("───┼───┼───")

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

display_board(game_board)
input()


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
    second = player2 if first == player1 else player1
    print(f"{first} goes first!")

    while True:
        mark = input(f"{first}, do you want X or O? ").upper()
        if mark in ["X", "O"]:
            break
        print("Type X or O")

    other_mark = "O" if mark == "X" else "X"
    print(f"{first} is {mark}, {second} is {other_mark}")

    return first, mark, second, other_mark


def tie_checker(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True




def get_player_move(board, first, mark):
    while True:
        display_board(board)
        move = input(f"{first} enter what row and column: ")
        row = int(move[0])
        column = int(move[1])
        if board[row][column] == "":
            board[row][column] = mark
            return
        print("Spot taken, try again")




def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    first, mark, second, other_mark = choose_first()
    players = [(first, mark), (second, other_mark)]
    turn = 0

    while True:
        name, m = players[turn]
        get_player_move(board, name, m)

        if check_winner(board, m):
            display_board(board)
            print(f"{name} wins!")
            return
        if tie_checker(board):
            display_board(board)
            print("It's a tie!")
            return

        turn = 1 - turn  





            
                
                    
                
        


