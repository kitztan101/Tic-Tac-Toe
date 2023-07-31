import random 
#display game board
def display_board(board):
    
    print(board[7]+ '|'+ board[8]+ '|' + board[9])
    print(board[4]+ '|'+ board[5]+ '|' + board[6])
    print(board[1]+ '|'+ board[2]+ '|' + board[3])

def start_game():
    print('Lets play tic tac toe!\n')

#player chooses X or O
def player_choice():
    choice = ''

    while choice != 'X' and choice != 'O':

        choice = input('What would you like to play as X or O: ').upper()

    player1 = choice

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)


#putting the sybomls on the board
def symbol_location(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def player_turn():

    coin = random.randint(0,1)

    if coin == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_position(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a location: '))

    return position

def play_again():

    return input('Play again? Y or N ').upper()

    


while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_choice()
    turn = player_turn()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y or N: ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display_board(the_board)
            position = player_position(the_board)
            symbol_location(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Its a tie!')
                    break    
                else:
                    turn = 'Player 2'

        else:
            display_board(the_board)

            position = player_position(the_board)

            symbol_location(the_board, player2_marker, position)

            if win_check(the_board, player2_marker,):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Its a tie!')
                    break
                    
                else:
                    turn = 'Player 1'

    if not play_again() == 'Y':
        break