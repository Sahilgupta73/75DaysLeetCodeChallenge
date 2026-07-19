class Solution {
public:

    bool valid(vector<int>& qty, int n, int mid) {
        int c = 0;
        for (int x : qty) {
            c += (x+mid-1) / mid;
            if (c > n) return false;
        }
        return true;
    }

    int minimizedMaximum(int n, vector<int>& quantities) {
        int l = 1, r = 1e5, ans = -1;
        while(l <= r) {
            int mid = l+(r-l)/2;
            if(valid(quantities,n,mid)) {
                ans = mid;
                r = mid - 1;
            }
            else {
                l = mid + 1;
            }
        }
        return ans;
    }
};