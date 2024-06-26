# https://github.com/KatkaMarcincakova/programko/

# - Funkcia inicializuje prázdne herné pole
def initialize_board():
    return [['.' for _ in range(4)] for _ in range(4)]

# - Funkcia vykreslí aktuálny stav herného poľa na štandartný výstup
def print_board(board):
    for row in board:
        print('|'.join(row))

    print("-" * (len(board[0]) * 2 - 1))
    print(" ".join(map(str, range(0, len(board[0])))))
    print("\n===================\n")

# - Funkcia položí krúžok hráča na do daného sĺpca
def drop_piece(col, player_char):
    for i in range(3, -1, -1):
        if board[i][col] == '.':
            board[i][col] = player_char
            return True

    return False

#- Funkcia overí vyhru v každom zo smerov
def check_win(board):
    # diagonaly
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] != '.':
        return True

    if board[0][3] == board[1][2] == board[2][1] == board[3][0] != '.':
        return True

    # riadky
    for i in range(4):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] != '.':
            return True

    # stlpce
    for i in range(4):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] != '.':
            return True
        
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

while (is_board_full() == False and check_win(board) == False):
    input_col = int(input('Zadaj stlpec: '))
    if drop_piece(input_col, get_current_char(x)) == True:
        print_board(board)
        x = not x
    else:
        print('Plny stlpec. Vyber iny')

if is_board_full():
    print('Remiza')
else:
    print(f'Vyhral {get_current_char(not x)}')
