class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int,int> map;
        for (int x : nums) {
            map[x]++;
        }
        vector<pair<int,int>> arr;
        for (auto [key,value] : map) {
            arr.push_back({value,key});
        }
        sort(arr.begin(),arr.end(), [](auto a,auto b){
            if (a.first != b.first) return a.first <  b.first;
            return a.second > b.second;
        });
        int j = 0;
        for (int i = 0;i<arr.size();i++) {
            while (arr[i].first--) {
                nums[j++] = arr[i].second;
            }
        }
        return nums;
    }
};