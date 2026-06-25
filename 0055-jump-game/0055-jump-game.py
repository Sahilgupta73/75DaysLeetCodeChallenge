class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination = len(nums) - 1 
        maxi = 0


        for i in range(0,len(nums)):
            if i >maxi:return False
            maxi = max(maxi,i+nums[i])
        return True