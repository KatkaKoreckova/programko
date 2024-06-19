# - Funkcia inicializuje prázdne herné pole
def initialize_board():
    return [[' . ' for _ in range(4)] for _ in range(4)]

# - Funkcia vykreslí aktuálny stav herného poľa na štandartný výstup
def print_board(board):
    for row in board:
        print('|'.join(row))

    print("-" * (len(board[0]) * 4 - 1))
    print(" " + "   ".join(map(str, range(1, len(board[0]) + 1))))

# - Funkcia položí krúžok hráča na do daného sĺpca
def drop_piece(board, col, player_char):
    return

#- Funkcia overí vyhru v každom zo smerov
def check_win(board):
    return

# - Funkcia zistí či je herné pole už plné a teda jední sa o remízu
def is_board_full(board):
    return

board = initialize_board()
print_board(board)
