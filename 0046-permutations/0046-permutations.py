class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        self.n = len(nums)

        self.generate(nums, [], [False] * self.n)

        return self.answer

    def generate(self, nums, current, vis):
        if len(current) == self.n:
            self.answer.append(current.copy())
            return

        for i in range(self.n):
            if vis[i]:
                continue

            vis[i] = True
            current.append(nums[i])

            self.generate(nums, current, vis)

            vis[i] = False
            current.pop()