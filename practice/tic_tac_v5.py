import sys

turn ="Player1"
game_on=True

def declare_board():
    global board
    global n
    print("Enter size of board (n)")
    n=int(input())
    board = [[' ']*n for _ in range(n)]

def print_board():
    global n
    for r in range(n):
        print(" | ".join(board[r]))
        print('-'*(n*n-1))

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

def main_game():
    global game_on
    global turn

    while(game_on):
        if turn=="Player1":
            get_correct_user_input(player1_name,player1_symbol)
            result=is_win_or_tie(player1_symbol)
            if result==Win:
                game_on =False
                print(player1_name, "Won")
                break
            elif result==Tie:
                game_on = False
                print("Its a Tie!!")
                break
            else:
                turn ="Player2"
        if turn=="Player2":
            get_correct_user_input(player2_name,player2_symbol)
            result=is_win_or_tie(player2_symbol)
            if result==Win:
                game_on =False
                print(player2_name, "Won")
                break
            elif result==Tie:
                game_on = False
                print("Its a Tie!!")
                break
            else:
                turn ="Player1"

    if game_on==False:
        play_again()

def get_correct_user_input(player_name,player_symbol):
    print(player_name+"'s turn")
    print("Enter row and col number")
    while True:
        try:
            p_in_r,p_in_c=input().split( )
            p_in_r=int(p_in_r)
            p_in_c=int(p_in_c)
        except ValueError:
            sys.stderr.write("Sorry, I didn't understand that.Please enter a valid index")
            continue
        if p_in_r>n-1 or p_in_r<0 or p_in_c>n-1 or p_in_c<0:
            sys.stderr.write("Wrong index, please choose within 0 and n")
            continue
        elif board[p_in_r][p_in_c]!=' ':
            sys.stderr.write("Cell already filled, please choose an empty cell")
            continue
        else:
            break
    board[p_in_r][p_in_c]=player_symbol
    print_board()

def is_win_or_tie(s):
    global Win
    global Tie
    Win=False
    Tie=False

#Check Each Row
    for r in range(n):
        flag_r=True
        for c in range(n):
            if board[r][c]!=s:
               flag_r=False
               break
        if flag_r==True:
            break
#Check Each Col
    for c in range(n):
        flag_c=True
        for r in range(n):
            if board[r][c]!=s:
                flag_c=False
                break
        if flag_c==True:
            break
#Check left diagonal
    r=0
    c=0
    flag_dl = True
    while r<n and c<n:
        if board[r][c]!=s:
            flag_dl=False
            break
        else:
            r+=1
            c+=1
#Check right diagonal
    r=0
    c=n-1
    flag_dr=True
    while r<n and c>=0:
        if board[r][c]!=s:
            flag_dr=False
            break
        else:
            r+=1
            c-=1

    if flag_r==True or flag_c==True or flag_dl==True or flag_dr==True:
        Win=True
        return Win
    else:
        for k in range(n):
            if ' ' in board[k]:
                break
            elif k==n-1:
                Tie=True
                return Tie

def play_again():
    global game_on
    print("Would you like to play again?")
    user = input()
    if user == 'y' or user == 'Y':
        game_on = True
        turn="Player1"
        seq()
    else:
        return None

def seq():
    declare_board()
    print_board()
    get_player_info()
    main_game()

seq()