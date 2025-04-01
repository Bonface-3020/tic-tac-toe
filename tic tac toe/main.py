
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    players = ["X", "O"]
    turn = 0
    winning_words = [
        "🎉 Victory! You crushed your opponent!",
        "🏆 You're the champ!",
        "🔥 Amazing win—you're unstoppable!"
    ]
    losing_words = [
        "💔 Better luck next time!",
        "😢 Oh no! You've been defeated.",
        "🤷‍♂️ Tough game—you'll get 'em next time!"
    ]

    while True:
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")
        try:
            
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))

          
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                print("Invalid move, try again!")
                continue

            
            board[row][col] = current_player
            print_board(board)

            
            if check_winner(board, current_player):
                print(f"Player {current_player} wins! {winning_words[turn % len(winning_words)]}")
                break

            
            if is_full(board):
                print("It's a draw! A close call!")
                break

          
            turn += 1
        except ValueError:
            print("Please enter a valid number.")

tic_tac_toe()