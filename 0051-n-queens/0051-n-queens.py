from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.answer = []
        self.n = n

        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)
        self.cols = [False] * n

        board = [['.' for _ in range(n)] for _ in range(n)]

        self.generate(0, board)

        return self.answer

    def generate(self, row, board):
        if row == self.n:
            self.answer.append([''.join(r) for r in board])
            return

        for col in range(self.n):
            d1 = row + col
            d2 = row - col + self.n - 1

            if self.cols[col] or self.diag1[d1] or self.diag2[d2]:
                continue

            board[row][col] = 'Q'
            self.cols[col] = True
            self.diag1[d1] = True
            self.diag2[d2] = True

            self.generate(row + 1, board)

            board[row][col] = '.'
            self.cols[col] = False
            self.diag1[d1] = False
            self.diag2[d2] = False