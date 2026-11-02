import random


def display_board(board):
    """
    Description: Printss the current tic tac toe board 

    Parameters:
     board:\

    Returns:
     None just prints the board
    """
    print("   1   2   3")
    for i in range(3):
        print(f"{i+1}  " + " | ".join(board[i]))
        if i < 2:
            print("  ───┼───┼───")


def tie_checker(board):
    """
    Description Checks if the board is completly full. If every spot is taken
    and nobody won, the game is a tie.

    Parameters:
     board: 

    Returns
     True if there are no empty spots left, False otherwise
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def check_winner(board, mark):
    """
    Description: Checks all 3 rows, all 3 columns, and both diagonals to see
    if the given mark has three in a row.

    Parameters
     board: 
     mark: 

    Returns:
     True if that mark has won, False if it hasnt
    """
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
    """
    Description: Asks both players for there names, makes sure the names are
    not the same then randomly picks who goes first.

    Parameters:
     None

    Returns:
    first player name, first player mark, second player name,
      second player mark
    """
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")
    while player2 == player1:
        player2 = input(" Names can't be the same, Player 2 pick another name: ")

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


def get_player_move(board, name, mark):
    """
    Description: Shows the board and asks the player to enter a move 
    Parameters:
     board 
     name
     mark

    Returns
     None the board is changed directly
    """
    while True:
        display_board(board)
        move = input(f"{name}, enter row then column (like 13): ")
        if move not in ["11", "12", "13", "21", "22", "23", "31", "32", "33"]:
            print("Not a valid spot, enter row then column, look at the board for reference")
            continue
        row = int(move[0]) - 1
        column = int(move[1]) - 1
        if board[row][column] == " ":
            board[row][column] = mark
            return
        print("Spot taken, try again")


def play_game():
    """
    Description: Runs one full game of tic tac toe. 

    Parameters:
     None

    Returns:
    the winners name, or "Tie" if nobody won
    """
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
            return name
        if tie_checker(board):
            display_board(board)
            print("It's a tie!")
            return "Tie"

        turn = 1 - turn



scores = {}

while True:
    winner = play_game()
    scores[winner] = scores.get(winner, 0) + 1

    print("Score:")
    for name in scores:
        print(f"  {name}: {scores[name]}")

    if input("Play again? (y/n) ").lower() != "y":
        break
