class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # sum_word = sum(nums[:k])

        # max_word = sum_word

        # for i in range(k, len(nums)):
        #     max_word = max_word + nums[i] - nums[i-k]
        #     max_word = max(max_word, sum_word)
        
        # return max_word/k
        
        sum_word = sum(nums[:k])

        max_word = sum_word

        for i in range(k, len(nums)):
            sum_word = sum_word + nums[i] - nums[i-k]
            max_word = max(max_word, sum_word)

        return max_word / k