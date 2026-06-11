class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        # if(nums[min] and nums[max]):
        return k*(max(nums) - min(nums))

            