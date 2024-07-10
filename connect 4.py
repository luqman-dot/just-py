board = [["-"] * 7 for _ in range(6)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def get_valid_index(prompt):
    while True:
        try:
            index = int(input(prompt))
            if 0 <= index <= 6:
                return index
            print("Must be a number 0 - 6 inclusive. Try again!")
        except ValueError:
            print("Must be a number between 0-6 inclusive! Try again!")

def game_is_over(board, turn):
    # Check horizontal
    for row in board:
        for i in range(4):
            if row[i] == row[i+1] == row[i+2] == row[i+3] == turn:
                return True

    # Check vertical
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == turn:
                return True

    # Check diagonal (left to right)
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == turn:
                return True

    # Check diagonal (right to left)
    for row in range(3, 6):
        for col in range(4):
            if board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3] == turn:
                return True

    return False

def place_piece(board, column, turn):
    for i in range(5, -1, -1):
        if board[i][column] == "-":
            board[i][column] = turn
            return

turn = "1"
while True:
    print_board(board)
    print("It is player " + turn + "'s turn.")
    column = get_valid_index("Choose a column (between 0-6 inclusive): ")
    place_piece(board, column, turn)
    
    if game_is_over(board, turn):
        print_board(board)
        print("Player " + turn + " wins!")
        print("Game is over!")
        break
    else:
        turn = "2" if turn == "1" else "1"
