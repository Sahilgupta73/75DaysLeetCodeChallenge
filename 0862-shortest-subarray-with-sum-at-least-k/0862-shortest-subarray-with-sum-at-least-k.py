from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Create prefix sum array of size n + 1
        # P[i] represents the sum of nums[0] to nums[i-1]
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            
        min_len = float('inf')
        dq = deque()  # Will store indices of the prefix sum array P
        
        for i in range(n + 1):
            # 1. Check if we found a valid subarray from front of the deque
            while dq and P[i] - P[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
                
            # 2. Maintain the monotonic increasing property from the back
            while dq and P[i] <= P[dq[-1]]:
                dq.pop()
                
            # 3. Add current index to the deque
            dq.append(i)
            
        return min_len if min_len != float('inf') else -1