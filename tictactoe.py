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
        
        change_player()  # changes player if above funtions have been satisfied 


    if winner == "X" or winner == "O":     # when the game has ended
        print (winner + " Wins, Well done! ")
    elif winner == None:   # if there is no winner 
        print ("The game has finished in a tie.")


def player_turn(current_player):
    position = input("Pick a position on the board from 1-9: ")

    position = int(position) -1   #Changes position from a sting to an interger, 1 has been subtracted from it to get the correct index

    board[position] = "X"  # x will be displayed in the chosen index position
    show_board()  # show board function called to display updated board with x marked in position chosen


def check_gameover():
    winner_checking()
    tie_checking()
    return

def winner_checking():
    return

def tie_checking():
    return

def change_player():
    return


play_game()



# board
# diplay board 
# play game
# handle player turn
# check win
 # check rows
 # check columns
 # check diagnals 
# check tie
# change player