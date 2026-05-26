class Solution:
    def numSubarraysWithSum(self, nums, goal):
        count = {0: 1}
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num

            need = prefix_sum - goal

            if need in count:
                ans += count[need]

            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return ans