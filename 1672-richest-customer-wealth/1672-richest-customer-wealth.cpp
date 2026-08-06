class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int n = accounts.size();
        int maxwealth = 0;
        for(int i= 0; i<n; i++){

            int m = accounts[i].size();

            vector<int> k = accounts[i];   
            int count = 0;
            for(int j=0; j<m; j++){
                count = count + accounts[i][j];
            }
            maxwealth = max(maxwealth,count);

        }
        return maxwealth;
    }
    
};