class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = cnt = 0
        for i in s:
            if i == 'L':
                balance += 1
            if i == 'R':
                balance -= 1
            if balance == 0:
                cnt += 1
        return cnt
