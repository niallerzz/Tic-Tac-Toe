# tick tac toe game

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]
# board layout as a list

# Global variable
game_in_progress = True
current_player = "X"
winner = None

# Function designed to draw out the board 
def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Function to control the game play

def play_game():

    instructions()

    show_board()

    

    while game_in_progress:

        player_turn(current_player) # function to deal with a single turn of a player
        
        winner_checking()
        
        # tie_checking() # function to check if the game is complete
        
        change_player() # changes player if above funtions have been satisfied 


    if winner == "X" or winner == "O":     # when the game has ended
        print ("###### Tic Tac Toe Champion is Player " + winner + " , Congradulations! ######")
    elif winner == None:   # if there is no winner 
        print ("The game has finished in a tie.")
    

def instructions():
    print("#### Welcome to Tic Tac Toe #####"),
    print("The aim of the game is for players to position their letters"),
    print("so that they make a continuous line of three vertically, horizontally, or diagonally"),
    print ("Best of luck!!")
    



def player_turn(current_player):


    board_location = input(current_player + " Player please choose a position on the board from 1-9: ")

    user_input = False  # user_input is a boolean value which 
    while not user_input:
        
        while board_location not in ["1","2","3","4","5","6","7","8","9"]:
            
            board_location = input(current_player + " Player please choose a position on the board from 1-9: ")
        
        board_location = int(board_location) -1  #Changes position from a sting to an interger, 1 will be subtracted from input it to get the correct index on the board. 
    
        if board[board_location] == "-": # if the choosen position is free and the True boolean it will break the loop
            user_input = True
        else:   # otherwise the player will be asked to choose a new position
            print("Board position already taken, please choose a different position")
    
    board[board_location] = current_player  # x will be displayed in the chosen index position
    show_board()  # show board function called to display updated board with x marked in position chosen


def winner_checking():
    global game_in_progress
    global winner

    game_winner = combination_check()
  
    if game_winner:
        winner = game_winner
    else:
        winner = None
    return

# check all winning combinations 
def combination_check():
    global game_in_progress

    a = board[0] == board[1] == board [2] != "-" # row 1
    b = board[3] == board[4] == board [5] != "-" # row 2
    c = board[6] == board[7] == board [8] != "-" # row 3
    d = board[0] == board[3] == board [6] != "-" # column 1
    e = board[1] == board[4] == board [7] != "-" # column 2
    f = board[2] == board[5] == board [8] != "-"
    g = board[0] == board[4] == board [8] != "-"
    h = board[6] == board[4] == board [2] != "-"
    

    if a or b or c or d or e or f or g or h:
        game_in_progress = False
    if a or d or g:
        return board[0]
    elif c or h:
        return board[6]
    elif b:
        return board[3]
    elif e:
        return board[1]
    elif f:
        return board[2]
    return
    


# def tie_checking():
#     global game_in_progress
#     if "-" not in board:
#         game_in_progress = False
#     return


def change_player():
    global current_player
    if current_player== "X":
        current_player= "O"
    elif current_player =="O":
        current_player= "X"
    return


play_game()

