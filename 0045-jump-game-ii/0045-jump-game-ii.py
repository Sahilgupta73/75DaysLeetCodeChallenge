from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        self.n = len(nums)
        self.dp = [-1] * self.n
        return self.find(nums, 0)

    def find(self, nums: List[int], i: int) -> int:
        if i == self.n - 1:
            return 0

        if self.dp[i] != -1:
            return self.dp[i]

        mini = float("inf")

        for j in range(i + 1, min(self.n - 1, i + nums[i]) + 1):
            curr = self.find(nums, j)
            mini = min(curr + 1, mini)

        self.dp[i] = mini
        return self.dp[i]


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         maxi = 0,curr = 0,count = 0

#         for i in range(0,len(nums)-1):
#             maxi = maxi