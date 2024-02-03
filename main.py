"""
TO-DO: 
- need to clarify concise moves to avoid repition
- add some comments and function definitions
"""

from utilities import generate_piece, print_board

# DEV_MODE = False

def move_left(game_board: [[int, ], ]) -> [[int, ], ]:
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

def move_right(game_board: [[int, ], ]) -> [[int, ], ]:
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

def move_up(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(len(game_board)):
        for row in reversed(range (1, len(game_board))):
            if game_board[row][col] != 0:
                if game_board[row-1][col] == 0:
                    game_board[row-1][col] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col] == game_board[row-1][col]:
                    game_board[row-1][col] += game_board[row][col]
                    game_board[row][col] = 0

def move_down(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(len(game_board)):
        for row in range((len(game_board))-1):
            if game_board[row][col] != 0:
                if game_board[row+1][col] == 0:
                    game_board[row+1][col] += game_board[row][col]
                    game_board[row][col] = 0
                elif game_board[row][col] == game_board[row+1][col]:
                    game_board[row+1][col] += game_board[row][col]
                    game_board[row][col] = 0

def game_won(game_board: [[int, ], ]) -> [[int, ], ]:
    for col in range(1, (len(game_board))-1):
        for row in range(1, (len(game_board))-1):   
            if game_board[row][col] == 2048:
                return True 
            
def game_over(game_board: [[int, ], ]) -> bool:
    for col in range((len(game_board))-1):
        for row in range((len(game_board))-1):
            if game_board[row][col] == 0:
                return False
            else:
                if game_board[row][col] != game_board[row][col-1]:
                    if game_board[row][col] != game_board[row][col+1]:
                        if game_board[row][col] != game_board[row-1][col]:
                            if game_board[row][col] != game_board[row+1]:
                                return True

def main(game_board: [[int, ], ]) -> [[int, ], ]:
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['col']] = piece['val']
    
    computerTurn = True

    while True:
        if computerTurn == True:
            piece = generate_piece(game_board)
            game_board[piece['row']][piece['col']] = piece['val']
            computerTurn = False

            if game_over(game_board):
                break
                
            print_board(game_board)

            move = input().lower()
            keys = ['w', 'a', 's', 'd', 'q']

            if move not in keys:
                move = input().lower()

            if move == 'q':
                print("Goodbye")
                break
            elif move == 'a':
                move_left(game_board)
            elif move == 'd':
                move_right(game_board)
            elif move == 'w':
                move_up(game_board)
            elif move == 's':
                move_down(game_board)
            
            if game_won(game_board) == True:
                break

            computerTurn = True
        
        return game_board
        return generate_piece




if __name__ == "__main__":
    print("Welcome to the 2048 game")
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
