class Solution {
public:
    void fwht(vector<long long>& a, bool inverse) {
        int n = a.size();

        for (int len = 1; 2 * len <= n; len <<= 1) {
            for (int i = 0; i < n; i += 2 * len) {
                for (int j = 0; j < len; j++) {
                    long long u = a[i + j];
                    long long v = a[i + j + len];

                    a[i + j] = u + v;
                    a[i + j + len] = u - v;
                }
            }
        }

        if (inverse) {
            for (long long &x : a) x /= n;
        }
    }

    int uniqueXorTriplets(vector<int>& nums) {
        const int MAXX = 2048;

        vector<long long> f(MAXX, 0);

        for (int x : nums) {
            f[x] = 1;  // presence of value
        }

        fwht(f, false);

        for (int i = 0; i < MAXX; i++) {
            f[i] = f[i] * f[i] * f[i];
        }

        fwht(f, true);

        int ans = 0;
        for (long long cnt : f) {
            if (cnt > 0) ans++;
        }

        return ans;
    }
};