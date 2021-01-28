import csv
import io
import re

CELL_MATCH  = re.compile(r"define-fun v\d+_\d+x\d+ \(\) Bool\n    true")
VAR_MATCH   = re.compile(r"v\d+_\d+x\d+")


def read_z3_model(model_path, enc="utf8"):

    with io.open(model_path, 'r', encoding=enc) as modelf:

        model_text = modelf.read()


    # board is the board itself
    # board_prototype is a 2d list,
    #   each inner list contains [value, row, col]
    #  board_size is the size of the board
    board = []
    board_prototype = []
    board_size = 0


    # Parse our file for matching positions
    cells = re.findall(CELL_MATCH, model_text)
    for cell in cells:

        nums = [int(n) for n in re.findall(r"\d+", cell)]

        board_prototype.append(nums)

        if nums[1] > board_size:

            board_size = nums[1]


    # Create a normal, albeit empty, board
    for i in range(0, board_size):
        board.append([0] * board_size)

    # Fill the board
    for val, row, col in board_prototype:
        board[col - 1][row - 1] = val

    return board


def write_board(board, csv_path):

    with open(csv_path, "w", newline="") as f:

        writer = csv.writer(f)

        for row in board:

            writer.writerow(row)


if __name__ == "__main__":

    board = read_z3_model("D:/Files/School/spring_2021/CS458/sudoku/output/25x25.out")
    write_board(board, "D:/Files/School/spring_2021/CS458/sudoku/output/25x25_solved.csv")
