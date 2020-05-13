class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        sum = 0
        for i in str(N):
            sum += pow(int(i), k)
        return sum == N
