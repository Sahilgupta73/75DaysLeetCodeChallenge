class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.generate(len(nums),nums)

    def generate(self,n,nums):
        if n == 0:
            return [[]]
        
        num = nums[n-1]

        faith = self.generate(n-1,nums)
        answer = faith.copy()

        for temp in faith:
            new_temp = temp.copy()
            new_temp.append(num)
            answer.append(new_temp)

        return answer
