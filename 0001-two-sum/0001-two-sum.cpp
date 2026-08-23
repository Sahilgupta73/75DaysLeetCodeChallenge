class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> myarr;
        
        for(int i=0; i<nums.size(); i++){
            for(int j=1; j<nums.size(); j++){
                if(i!=j){
                    if((nums[i]+ nums[j]) == target ){
                        myarr.push_back(i);
                        myarr.push_back(j);
                        break;
                    }
                }
            }
            
        }
        myarr.resize(2);
        return myarr ;
    }
};


    // for(int j=1; j<nums.size(); j++){
                
    //             if((nums[i]+ nums[j]) == target){
    //                 myarr.push_back(i);
    //                 myarr.push_back(j);
    //             }
                
    //         }