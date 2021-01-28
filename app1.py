board = ['_', '_', '_',
        '_', '_', '_',
        '_', '_', '_']

def display_board():
    print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

winner = None
game_on = True
current_player = "X"

#Play game
def play_game():
    display_board()
    while game_on:
        handle_turns(current_player)

        winning_condition()
        game_draw()

        choose_player()

    #when the game over, tell us who won the game or its a draw
    if winner == "X" or winner == "O":
        print(f'{winner} won')
    elif winner == None:
        print("Draw")

#Function for winning game
def handle_turns(player):
    #turns = 0
    #First player is "X", second player is "O"
    #Display which player's turn it is
    print(f"{player}'s turn")
    i = int(input("Enter your choice: "))
    turns = False
    while not turns:
    # turns must be between 1-9, if choosen above 9, then ask player to choose between 1-9
        while i not in range(10):
            i = input("choose between 1 to 9: ")
        i = int(i) - 1
        #if board index value is '_', then we are good to play
        if board[i] == '_':
            turns = True
        else:
            #if board index value is filled with "X" or "O", then we should choose another index
            print("Invalid move, play again")
    #Assign player to our board
    board[i] = player

    display_board()

#This function includes row_condition, column_condition and diagonal_condition
def winning_condition():
    global winner
    row_win = row_condition()
    column_win = column_condition()
    diagonal_win = diagonal_condition()
    if row_win:
        winner = row_condition()
    elif column_win:
        winner = column_condition()
    elif diagonal_win:
        winner = diagonal_condition()
    else:
        winner = None

def row_condition():
    global game_on
    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'
    if row_1 or row_2 or row_3:
        game_on = False
     #First row
    if row_1:
       # game_on = True
        return board[0]
    #Second row
    elif row_2:
       # game_on = True
        return board[3]
    #Third row
    elif row_3:
        #game_on = True
        return board[6]
    else:
        return None

def column_condition():
    global game_on
    column_1 = board[0] == board[3] == board[6] != '_'
    column_2 = board[1] == board[4] == board[7] != '_'
    column_3 = board[2] == board[5] == board[8] != '_'
    if column_1 or column_2 or column_3:
        game_on = False
    if column_1:
        #game_on = True
        return board[0]
    # Second row
    elif column_2:
        #game_on = True
        return board[1]
    # Third row
    elif column_3:
        #game_on = True
        return board[2]
    else:
        return None


def diagonal_condition():
    global game_on
    diagonal_1 = board[0] == board[4] == board[8]  != '_'
    diagonal_2 = board[2] == board[4] == board[6] != '_'
    if diagonal_1 or diagonal_2:
        game_on = False
    #Diagonal1
    if diagonal_1:
        #game_on = True
        return board[0]
        #Diagonal2
    elif diagonal_2:
        #game_on = True
        return board[2]
    else:
        return None

#When game is draw
def game_draw():
    global game_on
    if '_' not in board:
        game_on = False
        return True
    else:
        #game_on = True
        return False

#Choose between X or O
def choose_player():
    global current_player
    # choosing between "X"s or "O"s turns
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

play_game()
