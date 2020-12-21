# tick tac toe game
import time

board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]
# board layout as a list

# Global variable
game_in_progress = True   # boolean the determines that the game is still in progress
current_player = "X"      # the current player begins the game with and alternates between "X" and "O"
winner = False            # boolean value that is given to indicate there the is no winner to begin
count = 0
# Function designed to draw out the board 
def show_board():
    print(board[0] + "|" + board[1] + "|" + board[2])  # prints out the first row with the spaces separted by a line
    print(board[3] + "|" + board[4] + "|" + board[5])  # prints out the first row with the spaces separted by a line
    print(board[6] + "|" + board[7] + "|" + board[8])  # prints out the first row with the spaces separted by a line


# Function to control the game play

def play_game():

    instructions()  # instruction issue on the main screen

    show_board() # function is called to display an empty board at the beginning of the game

    

    while game_in_progress:  # loop while the game in progress is a True value

        player_turn(current_player) # function to deal with a single turn of a player
        
        winner_checking()  # calls winning check function that will run through all combinations to check for a winner
        
        tie_checking()    # calls the tie check function that checks if any remaining free spaces are available
        
        change_player() # changes player if above funtions have been satisfied 


    if winner == "X" or winner == "O":    # breaks loop if that winner check has found a winner
        print ("###### Tic Tac Toe Champion is Player " + winner + " , Congradulations! ######")
    
# play_again()
    
    
# instructive txt printed on entrance to game
def instructions():
    print("#### Welcome to Tic Tac Toe #####"),
    print("The aim of the game is for players to position their letters"),
    print("so that they make a continuous line of three vertically, horizontally, or diagonally"),
    print ("Best of luck!!")
    
# function that deals with a single turn of a player
def player_turn(current_player):

# player chooses position on the board to place mark
    board_location = input(current_player + " Player please choose a position on the board from 1-9: ")

    user_input = False 

    while not user_input: # user input loop that will break only when the correct position is input
        
        while board_location not in ["1","2","3","4","5","6","7","8","9"]: # if user input is not one of the strings in this list, they will asked for another input
            
            board_location = input() # will keep askin the user for 
        
        board_location = int(board_location) -1  #Changes position from a sting to an interger, 1 will be subtracted from input it to get the correct index on the board. 
    
        if board[board_location] == "-": # if the choosen position is free the boolean will be true it will break the loop
            user_input = True
        else:   # otherwise the player will be asked to choose a new position
            print("Board position already taken, please choose a different position: ")
    
    board[board_location] = current_player  # mark will be displayed in the chosen index position
  
    show_board()  # show board function called to display updated board

  

# checks for a global winner 
def winner_checking():
    global game_in_progress  # global variable
    global winner            # global variable

    game_winner = combination_check()         
  
    if game_winner:
        winner = game_winner
    else:
        winner = False
    return

# check all winning combinations 
def combination_check():
    global game_in_progress

    a = board[0] == board[1] == board [2] != "-" # row 1
    b = board[3] == board[4] == board [5] != "-" # row 2
    c = board[6] == board[7] == board [8] != "-" # row 3
    d = board[0] == board[3] == board [6] != "-" # column 1
    e = board[1] == board[4] == board [7] != "-" # column 2
    f = board[2] == board[5] == board [8] != "-" # column 3
    g = board[0] == board[4] == board [8] != "-" # diag 1
    h = board[6] == board[4] == board [2] != "-" # diag 2
    
# if any of the the above are True the game will stop and delcare a winner
    if a or b or c or d or e or f or g or h:
        game_in_progress = False
    if a or d or g:
        return board[0]  # only needs one index returned from combination to determine if "X" or "O" is the winner
    elif c or h:
        return board[6]  # only needs one index returned from combination to determine if "X" or "O" is the winner
    elif b:
        return board[3]  # only needs one index returned from combination to determine if "X" or "O" is the winner
    elif e:
        return board[1]  # only needs one index returned from combination to determine if "X" or "O" is the winner
    elif f:
        return board[2]  # only needs one index returned from combination to determine if "X" or "O" is the winner
    return
    

# checks if the board has any free spaces left, if not the game is considered a tie
def tie_checking():
    global winner, count, game_in_progress
    count += 1
    if count == 9 and not winner:
        print("The game has ended in a tie")
    else:
        return

# function that is called in the play game function that changes current player from "X" to "O"
def change_player():
    global current_player
    if current_player== "X":
        current_player= "O"
    elif current_player =="O":
        current_player= "X"
    return

# initiate game
play_game()



# def Ai_player():
#     global board
#     possibleMoves = [x for x, letter in enumerate(board) if letter == "-" and x != 0]
#     move = 0

#     cornersOpen = []
  
#     edgesOpen = []
    
    
#     def selectRandom(li):
#     import random
#     ln = len(li)
#     r = random.randrange(0,ln)
#     return li[r]
    