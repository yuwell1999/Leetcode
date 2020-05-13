class Solution:
    def countLetters(self, S: str) -> int:
        cnt = 1
        sum = 0
        for i in range(1, len(S)):
            if S[i] != S[i - 1]:
                sum += (cnt + 1) * cnt // 2
                cnt = 1
            else:
                cnt += 1
        sum += (cnt + 1) * cnt // 2
        return sum
