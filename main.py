import string
from GameState import GameState
from ai import get_best_move

alphabet = string.ascii_uppercase


def main():

    while True:
        prompt()
        repeat = input("\nGo Again? (y for yes, anything else for no): ")
        if repeat != "y":
            print("Exiting...")
            break


def get_processing_time():
    while True:
        user_input = input(
            "\nHow long should the computer think about its moves (in seconds)?: "
        )
        if user_input == "":
            return 5  # default to 5
        try:
            val = int(user_input)
            if 0 <= val <= 30:
                return val
            print("Invalid time")
        except ValueError:
            print("Invalid time")


def is_first():
    while True:
        goFirst = input("Would you like to go first? (y/n): ").strip().lower()
        if goFirst == "y":
            print("Going first")
            return True
        elif goFirst == "n":
            print("Going last")
            return False
        else:
            print("Invalid Input. Try Again")


def prompt():
    processingTime = get_processing_time()
    goFirst = is_first()
    state = GameState(goFirst)
    winner = None
    print()
    state.printBoard()
    print()
    if not goFirst:
        botMove(state, processingTime)
        winner = state.check_win()
        print()
        state.printBoard()

    while winner is None:
        userMove(state)
        winner = state.check_win()
        if winner is not None:
            break

        botMove(state, processingTime)
        winner = state.check_win()
        print()
        state.printBoard()

    state.printBoard()
    print()
    print(f"\nGame Over! The winner is {winner}!")


def userMove(state: GameState):
    while True:
        pos = ""
        while len(pos) != 2:
            pos = input("Choose your next move (e.g., A1): ")

        try:
            col = int(pos[-1])
            row = pos[0].upper()
            converted_row = alphabet.index(row)

            if state.make_move(converted_row, col - 1, "O"):
                break
            else:
                print("That space is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input format or out of bounds. Try again.")


def botMove(state: GameState, processingTime):
    move = get_best_move(state, processingTime)
    if move is None:
        return

    state.make_move(move[0], move[1], state.current_turn)


if __name__ == "__main__":
    main()
