class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int totalSum = 0;

        int currMax = 0;
        int maxSum = nums[0];

        int currMin = 0;
        int minSum = nums[0];

        for (int x : nums) {
            totalSum += x;

            // Kadane for maximum subarray sum
            currMax = max(x, currMax + x);
            maxSum = max(maxSum, currMax);

            // Kadane for minimum subarray sum
            currMin = min(x, currMin + x);
            minSum = min(minSum, currMin);
        }

        // If all elements are negative
        if (maxSum < 0) {
            return maxSum;
        }

        int circularSum = totalSum - minSum;

        return max(maxSum, circularSum);
    }
};