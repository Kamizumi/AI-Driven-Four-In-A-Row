import string

alphabet = string.ascii_uppercase


def main():
    board = [[0 for _ in range(8)] for _ in range(8)]  # test board
    printBoard(board)

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
    return processingTime, goFirst


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
