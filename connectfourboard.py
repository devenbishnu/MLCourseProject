import copy

#
# handles connect four game mechanics
#
class ConnectFour:
    # init board with 42 slots
    def __init__(self):
        self.board = [0 for _ in range(42)]

    # check if game is won or tied, and if won return ID of winner
    def is_won(self):
        for i in range(len(self.board)):
            if self.board[i] == 0:
                continue
            modulo = i % 6
            if (modulo == 0) or (modulo == 1):
                if (self.board[i] == self.board[i + 1]) and (
                        self.board[i] == self.board[i + 2]) and (
                        self.board[i] == self.board[i + 3]):
                    return self.board[i]
            if ((modulo == 0) or (modulo == 1) or (modulo == 2)) and (
                    i < 21):
                if (self.board[i] == self.board[i + 7]) and (
                        self.board[i] == self.board[i + 14]) and (
                        self.board[i] == self.board[i + 21]):
                    return self.board[i]
            if i < 24:
                if (self.board[i] == self.board[i + 6]) and (
                        self.board[i] == self.board[i + 12]) and (
                        self.board[i] == self.board[i + 18]):
                    return self.board[i]
            if ((modulo == 0) or (modulo == 1) or (modulo == 2)) and (
                    i > 17):
                if (self.board[i] == self.board[i - 5]) and (
                        self.board[i] == self.board[i - 10]) and (
                        self.board[i] == self.board[i - 15]):
                    return self.board[i]
        allfull = True
        for i in range(len(self.board)):
            if self.board[i] == 0:
                allfull = False
        if allfull:
            return 2
        return 0

    # put piece of player's color in first empty spot in column, otherwise invalid
    def place(self, column, player):
        if column in range(7):
            for i in range(6):
                if self.board[i + (6 * column)] == 0:
                    self.board[i + (6 * column)] = player
                    return True
        return False

    # return a copy of the board given a potential move
    def board_if(self, column, player):
        ifboard = copy.deepcopy(self.board)
        if column in range(7):
            for i in range(6):
                if self.board[i + (6 * column)] == 0:
                    ifboard[i + (6 * column)] = player
                    return ifboard
        return []

    # determine if a move will win the game
    def winning_move(self, column, player):
        ifboard = copy.deepcopy(self.board)
        self.place(column, player)
        if self.is_won() == player:
            self.board = ifboard
            return True
        self.board = ifboard
        return False

    # pretty-prints the board
    def print_board(self):
        mapping = [[5, 11, 17, 23, 29, 35, 41],
                   [4, 10, 16, 22, 28, 34, 40],
                   [3, 9, 15, 21, 27, 33, 39],
                   [2, 8, 14, 20, 26, 32, 38],
                   [1, 7, 13, 19, 25, 31, 37],
                   [0, 6, 12, 18, 24, 30, 36]]
        prettyboard = []
        for i in range(len(self.board)):
            if self.board[i] == 1:
                prettyboard.append('X')
            if self.board[i] == -1:
                prettyboard.append('O')
            if self.board[i] == 0:
                prettyboard.append('.')
        print("\n--------------")
        for j in mapping:
            print(prettyboard[j[0]] + ' ' + prettyboard[j[1]] + ' ' + prettyboard[j[2]] + ' ' + prettyboard[j[3]] + ' ' + prettyboard[j[4]] + ' ' + prettyboard[j[5]] + ' ' + prettyboard[j[6]])
        print("--------------")
        print("0 1 2 3 4 5 6\n")
