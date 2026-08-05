class Solution {
public:
    string triangleType(vector<int>& nums) {

        // Check if it is a valid triangle
        if (nums[0] + nums[1] <= nums[2] ||
            nums[0] + nums[2] <= nums[1] ||
            nums[1] + nums[2] <= nums[0]) {
            return "none";
        }

        // Equilateral
        if (nums[0] == nums[1] && nums[1] == nums[2]) {
            return "equilateral";
        }

        // Isosceles
        if (nums[0] == nums[1] ||
            nums[1] == nums[2] ||
            nums[0] == nums[2]) {
            return "isosceles";
        }

        // Scalene
        return "scalene";
    }
};