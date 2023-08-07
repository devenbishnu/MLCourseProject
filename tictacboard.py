import copy


#
# handles tic tac toe game mechanics
#
class TicTacToe:
    # init board with 9 spots
    def __init__(self):
        self.board = [0 for _ in range(9)]

    # check if game is won or tied, and if won return ID of winner
    def is_won(self):
        for i in range(len(self.board)):
            if self.board[i] == 0:
                continue
            modulo = i % 3
            if modulo == 0:
                if (self.board[i] == self.board[i + 1]) and (
                        self.board[i] == self.board[i + 2]):
                    return self.board[i]
            if i < 3:
                if (self.board[i] == self.board[i + 3]) and (
                        self.board[i] == self.board[i + 6]):
                    return self.board[i]
            if i == 4:
                if (self.board[i] == self.board[i - 4]) and (
                        self.board[i] == self.board[i + 4]):
                    return self.board[i]
                if (self.board[i] == self.board[i - 2]) and (
                        self.board[i] == self.board[i + 2]):
                    return self.board[i]
        return 0

    # put player's marker on spot if valid, otherwise return false
    def place(self, index, player):
        if index in range(len(self.board)) and self.board[index] == 0:
            self.board[index] = player
            return True
        return False

    # return a copy of the board given a potential move
    def board_if(self, index, player):
        ifboard = copy.deepcopy(self.board)
        if index in range(len(self.board)) and self.board[index] == 0:
            ifboard[index] = player
            return ifboard
        return copy.deepcopy(self.board)

    # determine if a move will win the game
    def winning_move(self, index, player):
        ifboard = copy.deepcopy(self.board)
        self.place(index, player)
        if self.is_won() == player:
            self.board = ifboard
            return True
        self.board = ifboard
        return False
