# Propositional sudoku
 Using z3, python, and propositional logic to solve a sudoku puzzle.

 This was an assignment for my university's *CS458: Formal Methods for Program Verification*.

# How does this work?
  Provided with a .csv of a sudoku puzzle (see the puzzles/ directory,) this Python script will generate z3 code to solve a sudoku puzzle. The script then attempts to run z3 to check for a solution to the puzzle, and save the solution as another .csv file.

  To test this script, run `python solver.py puzzles/hard.csv`

  This script assumes that you have z3 installed. You will need to edit the solver.ini file accordingly. If you need to install z3, you can find it here: https://github.com/Z3Prover/z3/releases/tag/z3-4.8.10

# Issues
  Please note that I have only tested this on my own machine and you may run into issues. Also, this script assumes you will provide a sudoku puzzle that can actually be solved, and will throw an error if there is no solution.

  Also, I think this script runs in time O(n^3). That's just a quick guess, but for any puzzles larger than 16 x 16, this script is impractical.
