class Solution {
public:
    int findLucky(vector<int>& arr) {
        map<int,int> mp;

        for(int i:arr){
            mp[i]++;
        }

        int ans = -1;
        for(auto it: mp){
            if(it.first== it.second){
                ans = it.first;
            }
        }
        return ans;
    }
};






















// map<int, int> mp;

//         // Count frequency
//         for (int num : arr) {
//             mp[num]++;
//         }

//         int ans = -1;

//         // Check lucky integers
//         for (auto it : mp) {
//             if (it.first == it.second) {
//                 ans = it.first;
//             }
//         }

//         return ans;

