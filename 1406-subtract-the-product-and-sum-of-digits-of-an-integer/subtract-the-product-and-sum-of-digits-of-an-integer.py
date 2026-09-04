class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        mul = 1
        temp = n
        ans = 0
        while n>0:
            r1 = n%10
            add += r1
            n//=10
        while temp>0:
            r2 = temp%10
            mul *= r2
            temp//=10
        ans = mul - add
        return ans