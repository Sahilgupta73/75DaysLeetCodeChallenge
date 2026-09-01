class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        arr = []
        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(nums[i])
        
        for j in range(len(arr),len(nums)):
            arr.append(0)
        
        nums[:] = arr

        