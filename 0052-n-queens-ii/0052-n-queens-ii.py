class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.n = n

        self.cols = [False] * n
        self.diag1 = [False] * (2 * n - 1)
        self.diag2 = [False] * (2 * n - 1)

        self.generate(0)

        return self.count

    def generate(self, row):
        if row == self.n:
            self.count += 1
            return

        for col in range(self.n):
            d1 = row + col
            d2 = row - col + self.n - 1

            if self.cols[col] or self.diag1[d1] or self.diag2[d2]:
                continue

            self.cols[col] = True
            self.diag1[d1] = True
            self.diag2[d2] = True

            self.generate(row + 1)

            # Backtracking
            self.cols[col] = False
            self.diag1[d1] = False
            self.diag2[d2] = False