import string

alphabet = string.ascii_uppercase


def main():
    board = [[0 for _ in range(8)] for _ in range(8)]  # test board
    printBoard(board)

    prompt()


def prompt():
    while True:
        goFirst = ""
        while goFirst not in ["y", "n"]:
            goFirst = input("\nWould you like to go first? (y/n): ").strip().lower()
            if goFirst == "y":
                print("Going first")
            elif goFirst == "n":
                print("Going last")
            else:
                print("Invalid Input. Try Again")


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
