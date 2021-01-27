#We are using list to create board for our game
list = ['_', '_', '_',
        '_', '_', '_',
        '_', '_', '_']

#Function to display board
def display_board():
    print('|' + list[0] + '|' + list[1] + '|' + list[2] + '|')
    print('|' + list[3] + '|' + list[4] + '|' + list[5] + '|')
    print('|' + list[6] + '|' + list[7] + '|' + list[8] + '|')

#Declaring global variables
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
    if winner == 'X'or winner == 'O':
        print(f'{winner} won')
    elif winner == None:
        print("Draw")

#Function for winning game
def handle_turns(player):
    turns = 0
    #First player is "X, second player is "Y
    #Display which player's turn it is
    print(f"{player}'s turn")
    i = int(input("Enter your choice: "))
    turns = False
    while not turns:
    # turns must be between 1-9, if choosen above 9, then ask player to choose between 1-9
        while i not in range(9):
            i = input("choose between 1 to 9: ")
        i = int(i) - 1
        #if list index value is '_', then we are good to play
        if list[i] == '_':
            turns = True
        else:
            #if list index value is filled with "X" or "O", then we should choose another index
            print("Invalid move, play again")
    #Assign player to our list
    list[i] = player
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
    if (list[0] == list[1] == list[2] or list[3] == list[4] == list[5] or list[6] == list[7] == list[8]) != '_':
        game_on = False
     #First row
    elif (list[0] == list[1] == list[2]) != '_':
        game_on = True
        return list[0]
    #Second row
    elif (list[3] == list[4] == list[5]) != '_':
        game_on = True
        return list[3]
    #Third row
    elif (list[6] == list[7] == list[8]) != '_':
        game_on = True
        return list[6]
    else:
        return None

def column_condition():
    global game_on
    if (list[0] == list[3] == list[6] or list[1] == list[4] == list[7] or list[2] == list[5] == list[8]) != '_':
        game_on = False
    #First Column
    elif (list[0] == list[3] == list[6]) != '_':
        game_on = True
        return list[0]
    #Second Column
    elif (list[1] == list[4] == list[7]) != '_':
        game_on = True
        return list[1]
    #Third column
    elif (list[2] == list[5] == list[8]) != '_':
        game_on = True
        return list[2]
    else:
        return None

def diagonal_condition():
    global game_on
    if (list[0] == list[4] == list[8] or list[2] == list[4] == list[6]) != '_':
        game_on = False
    #Diagonal1
    elif (list[0] == list[4] == list[8]) != '_':
        game_on = True
        return list[0]
        #Diagonal2
    elif (list[2] == list[4] == list[6]) != '_':
        game_on = True
        return list[2]
    else:
        return None

#When game is draw
def game_draw():
    global game_on
    if '_' not in list:
        game_on = False
        return True
    else:
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
