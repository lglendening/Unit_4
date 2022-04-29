
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def print_board():
    print(
        f"{board[0][0]} |{board[0][1]} |{board[0][2]} \n"
        "-------- \n"
        f"{board[1][0]} |{board[1][1]} |{board[1][2]} \n"
        "-------- \n"
        f"{board[2][0]} |{board[2][1]} |{board[2][2]} \n"
    )

def player_turn(name, symbol):
    valid_spot = False
    while not valid_spot:
        valid_row = False
        while not valid_row:
            row_choice = int(input(f"{name} choose a row  where to put your {symbol}.  ")) - 1
            if row_choice < 0 or row_choice > 2 :
                print(f"Invalid choice {name}")
            else:
                valid_row = True

        valid_colum = False
        while not valid_colum:
            colum_choice = int(input(f"{name} choose a collum where to put your {symbol}.  ")) - 1
            if colum_choice < 0 or colum_choice > 2:
                print(f"Invalid choice {name}")
            else:
                valid_colum = True

        if board[row_choice][colum_choice] == " ":
            board[row_choice][colum_choice] = symbol
        else:
            print(f"That space is occupied {name}")

def check_for_win():
    
    # check for row win
    for row in range(len(board)):
        if board[row][0] != " ":
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                return True

    #check for collum win
    for column in range(len(board)):
        colum_values = []
        for row in range(len(board)):
            colum_values.append(board[row][column])
        if colum_values[0] != " ":
            if colum_values[0] == colum_values[1] and colum_values[1] == colum_values[2]:
                return True

    #diagonal 
    
    if board[0][0] != " ":
        if board [0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True
    if board[0][2] != " ":
        if board [0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True


p1_name = input("Player 1 name : ")
p2_name = input("Player 2 name : ")

current_player = p1_name
current_symbol = "X"

print_board()

turns = 0
win = False
while turns < 9:
    player_turn(current_player, current_symbol)

    print_board()

    if check_for_win():
        print(f"{current_player} won the game!")
        win = True
        break

    if current_player == p1_name:
        current_player = p2_name
        current_symbol = "O"
    else:
        current_player = p1_name
        current_symbol = "X"

if not win:
    print("Game ends in a tie! ")