class Solution {
public:
    void reverseString(vector<char>& s) {
        // int n = s.size();
        // vector<char> mystring;
        // for(int i=n; i>=0; i++){
        //     mystring.push_back(i);
        // }
        reverse(s.begin(),s.end());
        
    }
};