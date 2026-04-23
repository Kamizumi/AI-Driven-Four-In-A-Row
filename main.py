import string

alphabet = string.ascii_uppercase


def main():
    board = [["0" for _ in range(8)] for _ in range(8)]  # test board
    printBoard(board)

    while True:
        prompt(board)
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


def prompt(board: list[list[int]]):
    processingTime = get_processing_time()
    goFirst = is_first()
    print()
    printBoard(board)
    print()
    if not goFirst:
        board = botMove()
    userMove(board)  # check if game ends here and loop
    botMove(board)
    print()
    printBoard(board)

    return processingTime, goFirst


def userMove(board: list[list[int]]):
    pos = ""
    while len(pos) != 2:
        pos = input("Choose your next move: ")
    col = int(pos[-1])
    row = pos[0]
    converted_row = alphabet.index(row)
    print(col)
    print(converted_row)
    board[converted_row][col - 1] = "O"


def botMove(board: list[list[int]]):
    pass


def printBoard(board: list[list[int]]):
    print("  ", end="")
    for i in range(1, 9):
        print(i, end=" ")
    print()
    for i, row in enumerate(board):
        print(f"{alphabet[i]} ", end="")
        for el in row:
            print(el, end=" ") if el == "O" or el == "X" else print("-", end=" ")
        print()


if __name__ == "__main__":
    main()
