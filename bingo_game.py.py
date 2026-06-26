import random

def print_board(b):
    print(f"{b[0]} | {b[1]} | {b[2]} | {b[3]} | {b[4]}\n"
          f"{b[5]} | {b[6]} | {b[7]} | {b[8]} | {b[9]}\n"
          f"{b[10]} | {b[11]} | {b[12]} | {b[13]} | {b[14]}\n"
          f"{b[15]} | {b[16]} | {b[17]} | {b[18]} | {b[19]}\n"
          f"{b[20]} | {b[21]} | {b[22]} | {b[23]} | {b[24]}")

while True:
    choice = input("\n1. START GAME\n2. EXIT\nChoice: ")
    if choice == '2': break
    if choice != '1': continue

    board = [i for i in range(1, 26)] # 1 se 25 ki list
    
    while True:
        print_board(board)
        # Player Move
        move = int(input("Enter position (1-25): ")) - 1
        if 0 <= move < 25 and isinstance(board[move], int):
            board[move] = 'X'
        else:
            print("Invalid move!")
            continue

        # Computer Move
        empty_cells = [i for i, x in enumerate(board) if isinstance(x, int)]
        if not empty_cells: break
        comp_move = random.choice(empty_cells)
        board[comp_move] = 'O'