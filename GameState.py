from itertools import count
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

    def copy(self):
        '''
        Creates a deep copy of the board for the AI 
        '''
        new_state = GameState()
        new_state.board = copy.deepcopy(self.board)
        new_state.current_turn = self.current_turn
        return new_state
        
    def is_terminal(self):
        '''
        Returns all valid moves
        '''
        valid_moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == "0":
                    valid_moves.append((r,c))
        return valid_moves
        
    def count_pieces_in_middle(self, piece):
        '''
        For evaluation purposes; Checks to see how many pieces are in columns 4 and 5 (3 and 4 based on index 0)
        '''
        count = 0
        mid_cols = [3,4]
        for row in range(8):
            for col in mid_cols:
                if self.board[row][col] == piece:
                    count += 1
        return count
        
    def horizontal_streak(self, piece, length):
        '''
        For evaluation purposes; 3 in a row is an imminent threat VS 2 in a row is setting up, etc.
        '''
        count = 0
        for row in range(8):
            for col in range(8):
                if all(self.board[row][col + i] == piece for i in range(length)):
                    count += 1
        return count
        
    def evaluate(self, board):
        result = self.check_win()

        if result == "X": return 10000
        if result == "O": return -10000

        score = 0

        #Uses horizontal streak of 3 poses an imminent threat to victory
        score += self.horizontal_streak("X", 3) * 1000
        score -= self.horizontal_streak("O", 3) * 1000

        #Horizontal streak of 2 is a setup but still a bit worrying
        score += self.horizontal_streak("X", 2) * 10
        score -= self.horizontal_streak("O", 2) * 10

        #Spots in the middle columns because they provide more value
        score += self.count_pieces_in_middle("X") * 10
        score -= self.count_pieces_in_middle("O") * 10

        return score




        
