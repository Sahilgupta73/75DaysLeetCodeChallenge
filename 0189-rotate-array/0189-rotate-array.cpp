class Solution {
    public:
    void rotate(vector<int> &arr, int k) {
         int n = arr.size();
         k = k%n;
        reverseArray(arr,0,n-1);
        reverseArray(arr,0,k-1);
        reverseArray(arr,k,n-1);
    }
    void reverseArray(vector<int> &arr,int left,int right) {
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            right--;
            left++;
        }
        
    }
};