import sys

class Board:
    # A -1 denotes unset, 0 denotes a "0" and 1 denotes a "X"
    # n is the dimension of the board. 
    def __init__(self, n = 3):
       self.board = [[-1] * n for _ in range(n)]
       sys.stderr.write("We are in the ctor with n = " + str(n) + "\n")
       sys.stderr.write("Initialized the board to " + str(self.board))

    def set(self, newboard):
       # 2nd TODO: Check that the newboard's dimension matches that of the board
       self.board = newboard ## NO CHECKS !!

    # Return 0 if 0 won, 1 if X won or -1 if no one has yet won
    def find_winner(self):
        # 1st TODO ..
        return -1


def dothething():
    board = Board()
    board.set([0, 1, 0], [1, 0, 0], [1, 1, 0])
    # - Populate the board in a bunch of moves
    winner = board.find_winner()
    if winner != -1:
        print("The game has been won by %s" % ("X" if winner == 1 else "0"))
    else:
        print("The game is not yet won")

if __name__ == '__main__':
    dothething()
