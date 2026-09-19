class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0

        while num>0:
            d = num%10
            y = num//10
            num = d+y
            if num < 10:
                return num
            
        # return num


        