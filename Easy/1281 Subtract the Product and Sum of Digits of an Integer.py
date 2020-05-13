class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum = 0
        while n > 0:
            tmp = n % 10
            mul *= tmp
            sum += tmp
            n = int(n / 10)
        return mul - sum
