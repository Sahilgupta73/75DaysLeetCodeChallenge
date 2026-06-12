# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         prefix_sum = 0
#         mp = {0: 1}

#         for num in nums:
#             prefix_sum += num

#             need = prefix_sum - k

#             if need in mp:
#                 count += mp[need]

#             mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

#         return count

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0: 1}
        prefix = 0
        ans = 0

        for x in nums:
            prefix += x
            ans += mp.get(prefix - k, 0)
            mp[prefix] = mp.get(prefix, 0) + 1

        return ans