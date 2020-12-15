# tick tac toe game

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]
# board layout as a list

game_in_progress = True
current_player = "X"
winner = None

def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function designed to show board


def play_game():

    show_board()

    while game_in_progress:

        player_turn(current_player) # function to deal with a single turn of a player
        
        check_gameover() # function to check if the game is complete
        
        change_player() # changes player if above funtions have been satisfied 


    if winner == "X" or winner == "O":     # when the game has ended
        print ("###### Tic Tac Toe Champion is Player " + winner + " , Congradulations! ######")
    elif winner == None:   # if there is no winner 
        print ("The game has finished in a tie.")
    
   


def player_turn(current_player):

    position = input(current_player + " Player please choose a position on the board from 1-9: ")

    user_input = False  # user_input is a boolean value which 
    while not user_input:
        
        while position not in ["1","2","3","4","5","6","7","8","9"]: # It 
            
            position = input()
        
        position = int(position) -1  #Changes position from a sting to an interger, 1 will be subtracted from input it to get the correct index on the board. 
    
        if board[position] == "-": # if the choosen position is free and the True boolean it will break the loop
            user_input = True
        else:   # otherwise the player will be asked to choose a new position
            print("Board position already taken, please choose a different position")
    
    board[position] = current_player  # x will be displayed in the chosen index position
    show_board()  # show board function called to display updated board with x marked in position chosen


def check_gameover():
    winner_checking()
    tie_checking()
    return

def winner_checking():
    global winner
    
    row_winner = check_rows()

    column_winner = check_columns()
    
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
# global "game still in progress"
    global game_in_progress

    row_a = board[0] == board[1] == board [2] != "-"
    row_b = board[3] == board[4] == board [5] != "-"
    row_c = board[6] == board[7] == board [8] != "-"

    if row_a or row_b or row_c:
        game_in_progress = False
    if row_a:
        return board[0]
    elif row_b:
        return board[3]
    elif row_c:
        return board[6]
    return

def check_columns():
    global game_in_progress

    column_a = board[0] == board[3] == board [6] != "-"
    column_b = board[1] == board[4] == board [7] != "-"
    column_c = board[2] == board[5] == board [8] != "-"

    if column_a or column_b or column_c:
        game_in_progress = False
    if column_a:
        return board[0]
    elif column_b:
        return board[1]
    elif column_c:
        return board[2]
    return
    

def check_diagonals():
    global game_in_progress

    diag_a = board[0] == board[4] == board [8] != "-"
    diag_b = board[6] == board[4] == board [2] != "-"
  

    if diag_a or diag_b:
        game_in_progress = False
    if diag_a:
        return board[8]
    elif diag_b:
        return board[2]
    return   

def tie_checking():
    global game_in_progress
    if "-" not in board:
        game_in_progress = False
    return

def change_player():
    global current_player
    if current_player== "X":
        current_player= "O"
    elif current_player =="O":
        current_player= "X"
    return


play_game()


