class Solution(object):
    # Sahil Gupta
    def twoSum(self, nums, target):
        num_map = {}   # dictionary to store number and its index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i