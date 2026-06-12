class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}   # prefix_sum : first index
        prefix = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in mp:
                ans = max(ans, i - mp[prefix])
            else:
                mp[prefix] = i

        return ans