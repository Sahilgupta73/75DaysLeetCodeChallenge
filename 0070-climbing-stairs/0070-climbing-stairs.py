# class Solution:
#     def climbStairs(self, n: int) -> int:
        
class Solution:
    def climbStairs(self, n: int) -> int:
        self.dp = [-1] * (n + 1)
        return self.find(n)

    def find(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0

        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.find(n - 1) + self.find(n - 2)
        return self.dp[n]