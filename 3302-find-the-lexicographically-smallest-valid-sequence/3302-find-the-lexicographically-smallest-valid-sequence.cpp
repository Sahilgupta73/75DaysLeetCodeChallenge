class Solution {
public:
    vector<int> validSequence(string word1, string word2) {

        int n = word1.size();
        int m = word2.size();

        if (m == 1)
            return {0};

        // suf[i] = first character of word2
        // that cannot be matched using word1[i...n-1]
        vector<int> suf(n + 1, m);

        int j = m - 1;

        for (int i = n - 1; i >= 0; i--) {

            if (j >= 0 && word1[i] == word2[j]) {
                j--;
            }

            suf[i] = j + 1;
        }

        vector<int> ans;

        j = 0;
        bool changed = false;

        for (int i = 0; i < n && ans.size() < m; i++) {

            // Character already matches
            if (word1[i] == word2[j]) {

                ans.push_back(i);
                j++;
            }

            // Character doesn't match
            else {

                // We already used our one change
                if (changed)
                    continue;

                // Check whether the remaining part can be completed
                if ((m - suf[i + 1]) + j + 1 >= m) {

                    ans.push_back(i);
                    j++;
                    changed = true;
                }
            }
        }

        if (ans.size() != m)
            return {};

        return ans;
    }
};