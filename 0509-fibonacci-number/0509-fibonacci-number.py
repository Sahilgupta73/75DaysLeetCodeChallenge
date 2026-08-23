class Solution(object):
    def fib(self, n):
        if(n ==0):
            return 0
        elif(n == 1):
            return 1
        
        first = 0
        second = 1
        for i in range(1,n+1):
            third = first + second

            first = second
            second = third
        
        return first
        