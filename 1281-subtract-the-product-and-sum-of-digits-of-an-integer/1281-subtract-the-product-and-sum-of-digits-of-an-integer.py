class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        total =0
        while n>0:
            d = n%10
            mul = mul*d
            total = total + d

            n = n//10

        return mul - total

            