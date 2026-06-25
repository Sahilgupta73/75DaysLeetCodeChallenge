class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for  x in bills:
            if x == 5:
                five = five + 1
            elif x == 10:
                if five == 0:
                   return False
                ten = ten +1
                five = five -1
            else:
                if five>=1 and ten>0:
                    ten = ten -1
                    five = five -1
                elif five>=3:
                    five  = five -3
                else:
                    return False

        return True


    
        # if bills[i] % 5 == 0:
        #     return True
        # else:
        #     return False