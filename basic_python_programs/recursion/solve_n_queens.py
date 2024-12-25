## n queens problem
# n queens is a problem of placing N chess queens on an N*N chessboard so that no wto queens attack each other
## they should not be in diagonal
## no two queens in same row or same column
## output is binary matrix
## is queen present 1 else 0
class Solution:
    def __init__(self, n):
        self.n = n
        self.col = set()
        self.posDiag = set()  # (r + c)
        self.negDiag = set()  # (r - c)
        self.res = []
        self.board = [["."] * n for _ in range(n)]

    def backtrack(self, r):
        if r == self.n:
            # Add a valid configuration to results
            copy = ["".join(row) for row in self.board]
            self.res.append(copy)
            return

        for c in range(self.n):
            if c in self.col or (r + c) in self.posDiag or (r - c) in self.negDiag:
                continue

            # Place queen
            self.col.add(c)
            self.posDiag.add(r + c)
            self.negDiag.add(r - c)
            self.board[r][c] = "Q"

            # Recurse to the next row
            self.backtrack(r + 1)

            # Remove queen (backtrack)
            self.col.remove(c)
            self.posDiag.remove(r + c)
            self.negDiag.remove(r - c)
            self.board[r][c] = "."

    def solveNQueens(self):
        self.backtrack(0)
        return self.res


# Example usage
q = Solution(4)
solutions = q.solveNQueens()
for solution in solutions:
    for row in solution:
        print(row)
    print()
