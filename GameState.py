import string

alphabet = string.ascii_uppercase


class GameState:
    def __init__(self, go_first=False):
        self.board = [["0" for _ in range(8)] for _ in range(8)]  # empty board
        self.current_turn = "O" if go_first else "X"

    def printBoard(self):
        board = self.board
        print("  ", end="")
        for i in range(1, 9):
            print(i, end=" ")
        print()
        for i, row in enumerate(board):
            print(f"{alphabet[i]} ", end="")
            for el in row:
                print(el, end=" ") if el == "O" or el == "X" else print("-", end=" ")
            print()

    def make_move(self, row: int, col: int, piece: str) -> bool:
        if self.board[row][col] == "0":
            self.board[row][col] = piece
            self.current_turn = "X" if piece == "O" else "O"
            return True
        return False

    def check_win(self) -> str | None:
        # horizontal
        for row in range(8):
            for col in range(5):
                if (
                    self.board[row][col] in ["O", "X"]
                    and self.board[row][col]
                    == self.board[row][col + 1]
                    == self.board[row][col + 2]
                    == self.board[row][col + 3]
                ):
                    return self.board[row][col]

        # vertical
        for col in range(8):
            for row in range(5):
                if (
                    self.board[row][col] in ["O", "X"]
                    and self.board[row][col]
                    == self.board[row + 1][col]
                    == self.board[row + 2][col]
                    == self.board[row + 3][col]
                ):
                    return self.board[row][col]

        return None
