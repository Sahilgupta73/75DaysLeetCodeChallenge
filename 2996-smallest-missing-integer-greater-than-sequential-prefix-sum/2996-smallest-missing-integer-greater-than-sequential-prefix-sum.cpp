class Solution {
public:
    int missingInteger(vector<int>& nums) {
        unordered_set<int>  set;
        int sum =  nums[0], n = nums.size();
        bool start = true;
        for (int i = 0;i<n;i++) {
            if (i>0 && start && nums[i]  == nums[i-1]+1) sum += nums[i];
            else if (i>0 && nums[i] != nums[i-1]+1) start = false;
            set.insert(nums[i]);
        }
        while (set.count(sum)) {
            sum++;
        }
        return sum;
    }
};