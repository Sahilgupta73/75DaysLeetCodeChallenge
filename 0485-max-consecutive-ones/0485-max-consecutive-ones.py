class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        maxi = 0 
        arr = []
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count = count + 1
                arr.append(count)
            else:
                count = 0
                arr.append(count)
        arr.sort()
        size = len(arr)
        return arr[size-1]
        