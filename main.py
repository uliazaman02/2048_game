"""
TO-DO: 
- need to clarify concise moves to avoid repition
- add some comments and function definitions
"""

# from utilities import generate_piece, print_board

# DEV_MODE = False

def moveLeft(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in reversed(range (1, len(game_board))):
        for row in range(len(game_board)):
            if game_board[row][col] != 0:
                if game_board[row][col-1] == game_board[row][col]: # is the if/elif necessary?
                    game_board[row][col-1] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col-1] == 0:
                    game_board[row][col-1] += game_board[row][col]
                    game_board[row][col] = 0
    for col in reversed(range (1, len(game_board))): # use previous nested for loop?
        for row in range(len(game_board)):
            if game_board[row][col] != 0:
                if game_board[row][col-1] == 0:
                    game_board[row][col-1] += game_board[row][col]
                    game_board[row][col] = 0
    print("bye")

def moveRight(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range((len(game_board)) - 1):
        for row in range(len(game_board)):
            if game_board[row][col] != 0:
                if game_board[row][col+1] == 0:
                    game_board[row][col+1] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col] == game_board[row][col+1]:
                    game_board[row][col+1] += game_board[row][col]
                    game_board[row][col] = 0
    for col in reversed(range((len(game_board))-1)):
        for row in range(len(game_board)):
            if game_board[row][col] != 0:
                if game_board[row][col+1] == 0:
                    game_board[row][col+1] += game_board[row][col]
                    game_board[row][col] = 0

def moveUp(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(len(game_board)):
        for row in reversed(range (1, len(game_board))):
            if game_board[row][col] != 0:
                if game_board[row-1][col] == 0:
                    game_board[row-1][col] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col] == game_board[row-1][col]:
                    game_board[row-1][col] += game_board[row][col]
                    game_board[row][col] = 0

def moveDown(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(len(game_board)):
        for row in range((len(game_board))-1):
            if game_board[row][col] != 0:
                if game_board[row+1][col] == 0:
                    game_board[row+1][col] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col] == game_board[row+1][col]:
                    game_board[row+1][col] += game_board[row][col]
                    game_board[row][col] = 0

def gameWon(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(1, (len(game_board))-1):
        for row in range(1, (len(game_board))-1):   
            if game_board[row][col] == 2048:
                return True 


if __name__ == "__main__":
    print("hi")
    moveLeft([[]])