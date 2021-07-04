import random

class Piece:
    def __init__(self, char):
        self._char = char

    def get_char(self):
        return self._char

    def __eq__(self, other):
        return self._char == other.get_char()

    def __str__(self):
        return self._char

class Player:

    def __init__(self, name, piece):
        self._name = name
        self._piece = piece

    def get_piece(self):
        return self._piece

    def get_name(self):
        return self._name

    def __str__(self):
        return "{}".format(self._piece)

    def __eq__(self, other):
        if other is None:
            return False
        return self._name == other.get_name() and self._piece == other.get_piece()

class Board:

    def __init__(self):
        self._board = [[None for _ in range(3)] for i in range(3)]

    def is_full(self):
        for i in self._board:
            for j in i:
                if j is None:
                    return False
        return True

    def is_valid_move(self, coord):
        x, y = coord
        return self._board[y][x] is None

    def put(self, player, coord):
        x, y = coord
        if self.is_valid_move(coord):
            self._board[y][x] = player

    def get(self, x, y):
        return self._board[y][x]

    def __str__(self):
        res = "     0   1   2  \n"
        ii = 0
        for i in self._board:
            res += "   +---+---+---+\n"
            res += "{}  ".format(ii)
            for j in i:
                ss = " "
                if j is not None:
                    ss = j
                res += "| {} ".format(ss)
            ii += 1
            res += "|\n"
        res += "   +---+---+---+\n"
        return res

    def same_w(self, y):
        return self.get(0, y) == self.get(1, y) == self.get(2, y)

    def same_h(self, x):
        return self.get(x, 0) == self.get(x, 1) == self.get(x, 2)

    def same_dtl(self):
        return self.get(0, 0) == self.get(1, 1) == self.get(2, 2)

    def same_dtr(self):
        return self.get(2, 0) == self.get(1, 1) == self.get(0, 2)

class Game:

    def __init__(self, player1, player2):
        self._board = Board()
        self._player1 = player1
        self._player2 = player2
        assert self._player1.get_piece().get_char() != self._player2.get_piece().get_char()

    def end(self):
        return self._board.is_full()

    def play(self):
        print(self._board)
        while (not self._board.is_full()):
            pmove = input("Player1 [x y]: ").strip().split()
            mv = (int(pmove[0]), int(pmove[1]))
            self._board.put(self._player1, mv)
            print(self._board)
            winner = self.winner()
            if winner != None:
                print("{} Won!".format(winner.get_name()))
                exit(0)
            # pmove = input("Player2 [x y]: ").strip().split()
            randomPoint = False
            while not randomPoint:
                mv = (random.randint(0, 2), random.randint(0, 2))
                randomPoint = self._board.is_valid_move(mv)
            self._board.put(self._player2, mv)
            print(self._board)
            winner = self.winner()
            if winner != None:
                print("{} Won!".format(winner.get_name()))
                exit(0)
        winner = self.winner()
        if winner is None:
            print("Draw")

    def winner(self):
        for i in range(3):
            if self._board.same_w(i):
                return self._board.get(0, i)
        for j in range(3):
            if self._board.same_h(j):
                return self._board.get(j, 0)
        if self._board.same_dtl():
            return self._board.get(0, 0)
        if self._board.same_dtr():
            return self._board.get(2, 0)
        return None


def main():
    print("TIC TAC TOE GAME")
    x = Piece('x')
    o = Piece('o')
    player1_name = input("Player1 name: ")
    player2_name = "IA"
    player1 = Player(player1_name, x)
    player2 = Player(player2_name, o)
    print(player1_name, "'s piece:", x)
    print(player2_name, "'s piece:", o)
    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()