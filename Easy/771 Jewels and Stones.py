class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for s in S:
            if s in J:
                cnt += 1
        return cnt
