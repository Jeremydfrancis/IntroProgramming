"""
Jeremy Francis
2026_04_06
Creating Board
"""
import random
from rich.console import Console

console = Console()

def create_board(rows,columns):
    """Creates and returns a 2D list representing the game board filled with "🔳" tiles."""
    board=[]
    for row in range(rows):
            board.append(["🔳"]*columns)
    return board
def show_board(board):
    """Prints the current board"""
    board_floors = "\n".join("".join(row) for row in board)
    return board_floors
def place_player_random(board,player):
    """Places the player at a random position on the board and updates their row and column."""
    ran_row = random.randint(0,len(board)-1)
    ran_col = random.randint(0,len(board[0])-1)
    player["row"]=ran_row
    player["column"]=ran_col
    board[ran_row][ran_col]="🧙"
    return board,player
def get_positive_integer(message):
    """Prompts the user with a message and loops until a valid positive integer is entered."""
    while True:
        try:
            user_input = int(input(message))
            if user_input <= 0:
                print(f"{user_input} Is Invalid: Please enter a number greater than 0")
                continue
            else:
                return user_input
        except ValueError:
            print("Please enter a positive integer")


