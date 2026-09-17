class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = 0;
        for (int i= 0; i<nums.size()-1; i++){
            if(nums[i]<nums[i+1]){
                n = i+1;
            }
        }
        return n;
    }

};