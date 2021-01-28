import csv
from math import sqrt
from sys import argv


def preview_file(csv_path):

    board = []

    with open(csv_path) as f:

        reader = csv.reader(f)

        for row in reader:

            board.append(row)


    height = len(board)
    width = len(board[0])

    print("Given a {0} x {1} board\n".format(width, height))

    if height != width:

        print("ERROR")
        print("Please give a board with the same width and height.")
        print("Additionally, please make the board size is equal to n^2 x n^2 (4, 9, 16, etc).")
        quit()

    if not sqrt(height).is_integer():

        print("ERROR")
        print("Please make the board size a power of 2.")
        quit()

    # For each row up to the last one...
    for row in board[:-1]:

        rowf = [str(n).center(3) for n in row]
        print("  ", "|".join(rowf))
        print("  ", "+".join(["---"] * len(row)))

    # And for the last row...
    rowf = [str(n).center(3) for n in board[-1]]
    print("  ", "|".join(rowf))
    print()

if __name__ == "__main__":

    if len(argv) == 1:
        print("ERROR")
        print("Please invoke this program as so:")
        print("python preview.py <path to .csv puzzle>")
        quit()

    path = argv[1]
    board = []

    print("Loading from {0} ...".format(path))

    preview_file(path)
