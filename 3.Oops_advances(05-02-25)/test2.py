def display_output(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_marker():
    marker = ' '
    while marker != 'O' and marker != 'X':
        marker = input("Player First choose Marker :O and X: ").upper()
    if marker == 'O':
        return ('O', 'X')
    return ('X', 'O')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[0] == mark and board[1] == mark and board[2] == mark) or
            (board[3] == mark and board[4] == mark and board[5] == mark) or
            (board[6] == mark and board[7] == mark and board[8] == mark) or
            (board[0] == mark and board[3] == mark and board[6] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[0] == mark and board[4] == mark and board[8] == mark) or
            (board[2] == mark and board[4] == mark and board[6] == mark))

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def board_is_full(board):
    for i in range(9):  # check all positions from 0 to 8
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 10
    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        position = int(input("Enter a number between 1 and 9: ")) - 1  
    return position

def replay():
    choice = input("Do you want to play again? Enter YES or NO: ").upper()
    return choice == "YES"

print("Welcome to Tic Tac Toe!")
while True:
    

    play_game = input("Ready to play? Enter Y or N: ").upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    this_board = [' '] * 9  
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn + ' will go first.')    

    while game_on:
        print(turn + "'s Turn")
        display_output(this_board)
        position = player_choice(this_board)
        if turn == 'Player 1':
            place_marker(this_board, player1_marker, position)
            if win_check(this_board, player1_marker):
                display_output(this_board)
                print("Player 1 Wins!!!")
                game_on = False
            else:
                if board_is_full(this_board):
                    display_output(this_board)
                    print("The game is a tie!")
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            place_marker(this_board, player2_marker, position)
            if win_check(this_board, player2_marker):
                display_output(this_board)
                print("Player 2 Wins!!!")
                game_on = False
            else:
                if board_is_full(this_board):
                    display_output(this_board)
                    print("The game is a tie!")
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
