# Define a function to solve the N-Queens problem.
def n_queens(n):
    # Initialize sets to keep track of occupied columns and diagonals.
    col = set()
    posDiag = set()  # Diagonals where the sum of row and column indices is constant.
    negDiag = set()  # Diagonals where the difference between row and column indices is constant.

    res = []  # Initialize a list to store solutions.

    # Create an empty chessboard.
    board = [["0"] * n for i in range(n)]

    # Define a recursive function to backtrack and find solutions.
    def backtrack(r):
        # If all rows are filled (r reaches n), a solution is found.
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        # Try placing a queen in each column of the current row.
        for c in range(n):
            # If the column or diagonals are already occupied, continue to the next column.
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            # Mark the column and diagonals as occupied.
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            # Recursively move on to the next row.
            backtrack(r + 1)

            # Backtrack by removing the queen and freeing up the column and diagonals.
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # Start the backtracking process from the first row.
    backtrack(0)

    # Print the solutions.
    for sol in res:
        for row in sol:
            print(row)
        print()

# Entry point of the program.
if __name__ == "__main__":
    # Call the n_queens function with N=8 to find and print solutions for the 8-Queens problem.
    n_queens(8)


'''
This code is an implementation of the N-Queens problem using a backtracking algorithm. The N-Queens problem is a classic combinatorial problem that asks for all possible ways to place N chess queens on an N×N chessboard so that no two queens threaten each other. Here's the code with comments:

Explanation of the concept used in this code:

- The N-Queens problem is solved using a backtracking algorithm. The goal is to explore all possible combinations of queen placements on an N×N chessboard while ensuring that no two queens threaten each other (i.e., they don't share the same row, column, or diagonal).

- The code maintains three sets (`col`, `posDiag`, and `negDiag`) to keep track of occupied columns and diagonals to ensure that queens are not attacking each other.

- The `backtrack` function is a recursive function that attempts to place queens row by row. It checks if a queen can be placed in a particular column and then moves on to the next row. If it successfully places all queens (when `r == n`), it records a solution.

- If a solution is found, it is stored in the `res` list and, at the end, all solutions are printed.

- The code explores all possible solutions through backtracking and finds all valid placements of N queens on the chessboard, where no two queens can attack each other.
'''