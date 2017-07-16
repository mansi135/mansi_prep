import sys

player_names = []
player_symbols = []

def declare_board():
    global board
    global n
    print("Enter size of board (n)")
    n = int(input())
    board = [[' '] * n for _ in range(n)]

def print_board():
    for r in range(n):
        s = " | ".join(board[r])
        print(s)
        print('-' * len(s))

def get_player_info():
    global player_symbols
    global player_names

    player1_name = input("Enter player1 name:")
    player2_name = input("Enter player2 name:")
    player_names = [player1_name, player2_name]
    while True:
        print(player_names[0], "Would you like to be X or 0?")
        symbol = input().upper()
        if symbol == 'X':
            other_symbol = '0'
        elif symbol == '0':
            other_symbol = 'X'
        else:
            print("Please enter a valid symbol, {} is not a symbol !" % (symbol))
            continue
        player_symbols = [symbol, other_symbol]
        break

class GameResult:
    def __init__(self, terminated, who_won):
        self.terminated = terminated
        assert who_won >= -1 and who_won <= 1
        self.who_won = who_won

    def is_game_on(self):
        return not self.terminated

    def is_won(self):
        return self.terminated and self.who_won >= 0

    def __repr__(self):
        return "({}, {})".format(self.terminated, self.who_won)

def main_game():
    game_on = True
    player_one_playing = True

    while (game_on):
        print_board()
        get_correct_user_input(0 if player_one_playing else 1)
        game_result = get_game_result()
        game_on = game_result.is_game_on()
        if not game_on:
            if game_result.who_won == -1:
                print("Its a Tie!!")
            else:
                print(player_names[game_result.who_won], "Won")
        else:
            player_one_playing = not player_one_playing

def get_correct_user_input(turn):
    print(player_names[turn] + "'s turn")
    print("Enter row and col number")
    while True:
        try:
            p_in_r, p_in_c = input().split()
            p_in_r = int(p_in_r)
            p_in_c = int(p_in_c)
        except ValueError:
            sys.stderr.write("Sorry, I didn't understand that.Please enter a valid index")
            continue
        if p_in_r > n - 1 or p_in_r < 0 or p_in_c > n - 1 or p_in_c < 0:
            sys.stderr.write("Wrong index, please choose within 0 and n\n")
            continue
        elif board[p_in_r][p_in_c] != ' ':
            sys.stderr.write("Cell already filled, please choose an empty cell")
            continue
        else:
            break
    board[p_in_r][p_in_c] = player_symbols[turn]

def check_line(start_r, start_c, del_r, del_c):
    r = start_r
    c = start_c
    symbols_in_row = set()
    for _ in range(n):
        symbols_in_row.add(board[r][c])
        r += del_r
        c += del_c

    if ' ' in symbols_in_row:
        return GameResult(False, -1)
    elif len(symbols_in_row) == 1:
        # Someone won a row, lets check who
        return GameResult(True, player_symbols.index(list(symbols_in_row)[0]))
    else:
        assert len(symbols_in_row) == 2
        return GameResult(True, -1)

# This can be tersified up even further by definining lines to iterate upon
# we can decouple the code that checks the lines vs the code that generates the lines to iterate upon
def get_game_result():
    lines = []
    for r in range(n):
        lines.append((r, 0, 0, 1))  # horizontal row

    for c in range(n):
        lines.append((0, c, 1, 0))  # vertical column

    lines.append((0, 0, 1, 1))  # left diag
    lines.append((0, n - 1, 1, -1))  # right diag

    unfilled_lines = 0
    for line in lines:
        game_result = check_line(*line)
        sys.stderr.write("For line {}, the result is {}\n".format(line, game_result))
        if game_result.is_won():
            return game_result
        elif not game_result.terminated:
            unfilled_lines += 1

    # There are no winners
    if unfilled_lines > 0:
        # There were unfilled lines, so it can't be a tie
        return GameResult(False, -1)
    else:
        # All lines are tied, and hence the game is tied
        return GameResult(True, -1)

def play_again():
    print("Would you like to play again?")
    user = input()
    return user.upper() == 'Y'

def play_one_time():
    declare_board()
    get_player_info()
    main_game()

def seq():
    while True:
        play_one_time()
        if not play_again():
            break

seq()