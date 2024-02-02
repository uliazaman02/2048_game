import random

def generate_piece():
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    val = random.choice([2, 4])

    piece = {'row': row, 'col': col, 'val': val}
    return piece
