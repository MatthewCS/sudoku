from sudoku import converter, generator, preview

import configparser
import csv
from math import sqrt
import os
import sys


def load_board(csv_path):

    board = []

    with open(csv_path) as f:

        reader = csv.reader(f)

        for row in reader:

            board.append(row)

    return board


def get_code_path(config, board_file_name):

    fname = os.path.basename(board_file_name)
    base = os.path.splitext(fname)[0]
    return config["PATHS"]["CodePath"].format(base)


def get_output_path(config, board_file_name):

    fname = os.path.basename(board_file_name)
    base = os.path.splitext(fname)[0]
    return config["PATHS"]["OutputModelPath"].format(base)


def get_csv_path(config, board_file_name):

    fname = os.path.basename(board_file_name)
    base = os.path.splitext(fname)[0]
    return config["PATHS"]["OutputCSVPath"].format(base)


if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("ERROR")
        print("Please invoke this program as so:")
        print("python preview.py <path to .csv puzzle>")
        quit()

    print("Loading from {0} ...".format(sys.argv[1]))

    board = load_board(sys.argv[1])
    config = configparser.ConfigParser()
    config.read_file(open("./solver.ini"))
    code_path = get_code_path(config, sys.argv[1])
    out_path = get_output_path(config, sys.argv[1])
    csv_path = get_csv_path(config, sys.argv[1])


    height = len(board)
    width = len(board[0])

    if height != width or not sqrt(height).is_integer():

        print("ERROR")
        print("Please make the board's width and height equal.")
        print("Please also make the board size equal to n^2 x n^2 (4, 9, 16, etc).")
        print("You provided a {0} x {1} board\n".format(width, height))
        quit()


    code = generator.get_code(board)

    with open(code_path, "w") as f:

        f.write(code)

    print("Wrote to {0}".format(code_path))


    print("Running z3...")
    os.system("{0} {1} > {2}".format(config["PATHS"]["Z3path"],
                                      code_path, out_path))
    print("Wrote resulting model to {0}".format(out_path))
    print()


    print("Reading model file...")
    solved_board = converter.read_z3_model(out_path)
    converter.write_board(solved_board, csv_path)
    print("Wrote solution to file {0}".format(csv_path))
    print()

    preview.preview_file(csv_path)
