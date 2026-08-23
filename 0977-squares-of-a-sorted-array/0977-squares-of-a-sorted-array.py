class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr1 = []
        for i in range(len(nums)):
            nums[i] = nums[i] *nums[i]
            arr1.append(nums[i])
        
        arr1.sort()
        return arr1