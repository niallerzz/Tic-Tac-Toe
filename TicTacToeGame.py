PLAYERS = ["X", "O"]

def display_board(board):
        print board[0][0:3]
        print board[1][0:3]
        print board[2][0:3]

def create_empty_board():
        return [[None, None, None], [None, None, None], [None, None, None]]

def board_is_full(board):
        for row in board:
                if None not in board:
                        return True


def winner(board):
        if board[0][0] == board[0][1] == board[0][2] != None:
                return board[0][0]
        elif board[1][0] == board[1][1] == board[1][2] != None:
                return board[1][0]
        elif board[2][0] == board[2][1] == board[2][2] != None:
                return board[2][0]
        elif board[0][0] == board[1][0] == board[2][0] != None:
                return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1] != None:
                return board[0][1]
        elif board[0][2] == board[1][2] == board[2][2] != None:
                return board[0][2]
        elif board[0][0] == board[1][1] == board[2][2] != None:
                return board[0][0]
        else:
                return None

def game_over(board):
        if board_is_full(board) == True:
                return True
def player_turn(board, playerid):
    """ Ask the player to select a coordinates for their next move. The player needs to select a row and a column. If the coordinates the player selects are outside of the board, or are already occupied, they need to be prompted to select coordinates again, until their input is valid."""
    return 1, 1 # by default, return row 1, column 1 as the player's desired location on the board; you need to implement this

def play():
    """ This is the main function that implements a hot seat version of Tic Tac Toe."""
    # the code below is just an example of how you could structure your play() function
    # if you implement all the functions above correctly, this function will work
    # however, feel free to change it if you want to organize your code differently
    board = create_empty_board()
    display_board(board)
    current_player = 0
    while not game_over(board):
        board = player_turn(board, PLAYERS[current_player])
        current_player = (current_player + 1) % len(PLAYERS)
        display_board(board)
    who_won = winner(board)
    if who_won is None:
        print "The game was a tie."
    else:
        print "The winning player is", who_won

if __name__ == "__main__":
    play()


    def instructions():
    print("#### Welcome to Tic Tac Toe #####"),
    print("The aim of the game is for players to position their letters"),
    print("so that they make a continuous line of three vertically, horizontally, or diagonally"),
    print ("Best of luck!!")
    