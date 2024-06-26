# - Funkcia inicializuje prázdne herné pole
def initialize_board():
    return [['.' for _ in range(4)] for _ in range(4)]

# - Funkcia vykreslí aktuálny stav herného poľa na štandartný výstup
def print_board(board):
    for row in board:
        print('|'.join(row))

    print("-" * (len(board[0]) * 2 - 1))
    print(" ".join(map(str, range(0, len(board[0])))))
    print("\n =================== \n")

# - Funkcia položí krúžok hráča na do daného sĺpca
def drop_piece(col, player_char):
    for i in range(3, -1, -1):
        if board[i][col] == '.':
            board[i][col] = player_char
            return True

    return False

#- Funkcia overí vyhru v každom zo smerov
def check_win(board):
    return False

# - Funkcia zistí či je herné pole už plné a teda jedna sa o remízu
def is_board_full():
    for row in board:
        if '.' in row:
            return False
    return True

def get_current_char(x):
    if x:
        return 'X'
    return 'O'

x = True
board = initialize_board()
print_board(board)
