class Solution {
    vector<vector<int>> answer;
    int n;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        generate(nums,vector<int>(),vector<bool>(n,false));
        return answer;
    }
    void generate(vector<int>& nums,vector<int> current,vector<bool> vis) {
        if (current.size() == n) {
            answer.push_back(current);
            return;
        }
        for (int i = 0;i<n;i++) {
            if (vis[i]) continue;
            vis[i] = true;
            current.push_back(nums[i]);
            generate(nums,current,vis);
            vis[i] = false;
            current.pop_back();
        }
    }
};