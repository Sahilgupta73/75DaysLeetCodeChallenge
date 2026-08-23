class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        // int num = numBottles % numExchange;
        // num = num +1 + numBottles;
        // return num;
        // int ans= numBottles + 
        // int remainder = numBottles%numExchange;
        // int qua = numBottles/numExchange
        // if((remainder + qua) >numExchange){

        // }
        int ans= numBottles;
        while(numBottles>=numExchange){
            int newBottles = numBottles / numExchange;
            int remExchange= numBottles%numExchange;
            ans = ans + newBottles;
            numBottles = newBottles+ remExchange;
        }

        return ans;

    }
};