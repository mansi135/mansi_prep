import sys

board =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn ="Player1"
game_on=True

def print_board():
    global board
    print(board[0] + " | " +board[1] + " | " +board[2])
    print("----------")
    print(board[3] + " | " +board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " +board[7] + " | " + board[8])


def get_player_info():
    global player1_name
    global player1_symbol
    global player2_name
    global player2_symbol

    player1_name=input("Enter player1 name:")
    player2_name=input("Enter player2 name:")
    print(player1_name, "Would you like to be X or 0?")
    player1_symbol = input().upper()
    if player1_symbol=='X':
        player2_symbol='0'
    else:
        player2_symbol='X'


def get_input_and_check_valid():
    global game_on
    global turn
    global player1_name
    global player1_symbol
    global player2_name
    global player2_symbol

    while(game_on):
        if turn=="Player1":
            print(player1_name+"'s turn")
            while True:
                try:
                    p_in=int(input())
                except ValueError:
                    sys.stderr.write("Sorry, I didn't understand that.Please enter a valid index")
                    continue
                if p_in>8 or p_in<0:
                    sys.stderr.write("Wrong index, please choose within 0 and 8")
                    continue
                elif board[p_in]!=' ':
                    sys.stderr.write("Cell already filled, please choose an empty cell")
                    continue
                else:
                    break
            board[p_in]=player1_symbol
            refresh_and_display_board(p_in,player1_symbol)
            if (is_win_or_tie(player1_symbol)):
                game_on =False
                print(player1_name, "Won")
                break
            else:
                turn ="Player2"

        if turn=="Player2":
            print(player2_name+"'s turn")
            p_in=int(input())
            if board[p_in]!=' ':
                print("Wrong input, please choose the empty cell")
            else:
                board[p_in]=player2_symbol
                refresh_and_display_board(p_in,player2_symbol)
                if (is_win_or_tie(player2_symbol)):
                    game_on =False
                    print(player2_name, "Won")
                    break
                else:
                    turn ="Player1"


def refresh_and_display_board(p_in,player_symbol):
    board[p_in]=player_symbol
    print_board()


def is_win_or_tie(s):
    win=False
    Tie=False
    if board[0] == s and board[1] == s and board[2] == s or \
       board[3] == s and board[4] == s and board[5] == s or \
       board[6] == s and board[7] == s and board[8] == s or \
       board[0] == s and board[3] == s and board[6] == s or \
       board[1] == s and board[4] == s and board[7] == s or \
       board[2] == s and board[5] == s and board[8] == s or \
       board[0] == s and board[4] == s and board[8] == s or \
       board[6] == s and board[4] == s and board[2] == s:
        win=True
    elif " " not in board:
        Tie=True

    return (win or Tie)


print_board()
get_player_info()
get_input_and_check_valid()


'''
1) general nxn board and index using r,c
2) add replay option
'''



