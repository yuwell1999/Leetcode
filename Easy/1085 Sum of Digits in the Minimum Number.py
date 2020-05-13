class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min = A[0]

        for i in range(1, len(A)):
            if A[i] < min:
                min = A[i]

        sum = 0
        while min != 0:
            sum += min % 10
            min = min // 10

        if sum % 2 == 0:
            return 1
        else:
            return 0
