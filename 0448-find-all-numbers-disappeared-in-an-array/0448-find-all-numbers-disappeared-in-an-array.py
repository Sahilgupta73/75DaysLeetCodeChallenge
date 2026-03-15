class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark visited numbers
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Collect missing numbers
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result