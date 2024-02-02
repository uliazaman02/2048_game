import random

def generate_piece(game_board: [[int, ], ]) -> dict:
    row = random.randint(0, len(game_board)-1)
    col = random.randint(0, len(game_board)-1)
    val = random.choice([2, 4])

    piece = {'row': row, 'col': col, 'val': val}
    return piece
