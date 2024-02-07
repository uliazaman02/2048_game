import random

def generate_piece(game_board: [[int, ], ]) -> dict:
    row = random.randint(0, len(game_board)-1)
    col = random.randint(0, len(game_board)-1)
    val = random.choice([2, 4])

    piece = {'row': row, 'col': col, 'val': val}
    return piece

def print_board(game_board: [[int, ], ]) -> [[int, ], ]:
    for row in range(len(game_board)):
        rowOut = ""
        for col in range(len(game_board)):
            rowOut += str(game_board[row][col])
            rowOut += " | "
        print(rowOut)
        print("---------------")
            