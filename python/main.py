"""
TO-DO: 
- need to clarify concise moves to avoid repition
- add some comments and function definitions
- game_over not working

[8, 0, 4, 0] -> moveRight -> [0, 8, 0, 4]
[0, 8, 2, 8] -> moveLeft -> [16, 2, 2, 0]
[0, 4, 0, 4] -> moveLeft -> [4, 0, 0, 0]
[4, 2, 0, 2] -> moveDown -> [0, 0, 0, 8]
[2, 4, 8, 2] -> moveLeft -> [4, 4, 8, 0]
[0, 2, 0, 4] -> moveUp -> 
"""

from utilities import generate_piece, print_board

def move_left(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    want to start traversing from left hand side
    then another loop to move over all the 0s
    """
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] != 0:
                for newCol in range(col+1, len(game_board)):
                    if game_board[row][col] == game_board[row][newCol]:
                        game_board[row][col] *= 2
                        game_board[row][newCol] = 0
                        break
                    if game_board[row][newCol] != 0:
                        break
    for row in range(len(game_board)):
        for col in reversed(range(1, len(game_board))):
            if (game_board[row][col] != 0) & (game_board[row][col-1] == 0):
                game_board[row][col-1] = game_board[row][col]
                game_board[row][col] = 0

def move_right(game_board: [[int, ], ]) -> [[int, ], ]:
    for row in range(len(game_board)):
        for col in reversed(range(len(game_board))):
            if game_board[row][col] != 0:
                for newCol in reversed(range(col)):
                    if game_board[row][col] == game_board[row][newCol]:
                        game_board[row][col] *= 2
                        game_board[row][newCol] = 0
                        break
                    if game_board[row][newCol] != 0:
                        break
    for row in range(len(game_board)):
        for col in reversed(range(1, len(game_board))):
            if game_board[row][col] == 0:
                found = False
                for newCol in reversed(range(col)):
                    if (game_board[row][newCol] != 0) & (found == False):
                        found = True
                        game_board[row][col] = game_board[row][newCol]
                        game_board[row][newCol] = 0

def move_up(game_board: [[int, ], ]) -> [[int, ], ]:
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] != 0:
                for newRow in range(row+1, len(game_board)):
                    if game_board[row][col] == game_board[newRow][col]:
                        game_board[row][col] *= 2
                        game_board[newRow][col] = 0
                        break

    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if (game_board[row][col] != 0):
                for newRow in range(0, row):
                    if game_board[newRow][col] == 0:
                        game_board[newRow][col] = game_board[row][col]
                        game_board[row][col] = 0
                        break

def move_down(game_board: [[int, ], ]) -> [[int, ], ]:
    for row in reversed(range(len(game_board))):
        for col in range(len(game_board)):
            if game_board[row][col] != 0:
                for newRow in reversed(range(row)):
                    if game_board[row][col] == game_board[newRow][col]:
                        game_board[row][col] *= 2
                        game_board[newRow][col] = 0
                        break
    for row in range(len(game_board)-1):
        for col in range(len(game_board)):
            if (game_board[row][col] != 0) & (game_board[row+1][col] == 0):
                game_board[row+1][col] = game_board[row][col]
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
    return True
            # else:
            #     if game_board[row][col] != game_board[row][col-1]:
            #         if game_board[row][col] != game_board[row][col+1]:
            #             if game_board[row][col] != game_board[row-1][col]:
            #                 if game_board[row][col] != game_board[row+1]:
            #                     return True


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    for i in range(2):
        piece = generate_piece(game_board)
        game_board[piece['row']][piece['col']] = piece['val']

    while True:
        if game_over(game_board):
            print("Game over")
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
            print("Game Won")
            break
        piece = generate_piece(game_board)
        game_board[piece['row']][piece['col']] = piece['val']

    return game_board



if __name__ == "__main__":
    print("Welcome to the 2048 game")
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])