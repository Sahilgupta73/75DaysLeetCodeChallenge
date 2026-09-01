class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        vector<int> arr1;
        for(int i=0; i<nums.size(); i++){
            if (nums[i] != 0){
                arr1.push_back(nums[i]);
            }
        }
        for(int j=arr1.size(); j<nums.size(); j++){
            arr1.push_back(0);
        }
        nums = arr1;
    }
};