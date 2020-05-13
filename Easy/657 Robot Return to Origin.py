class Solution:
    def judgeCircle(self, moves: str) -> bool:
        balanceX = balanceY = 0
        for i in moves:
            if i == 'U':
                balanceY += 1
            elif i == "D":
                balanceY -= 1
            elif i == 'L':
                balanceX += 1
            elif i == 'R':
                balanceX -= 1

        if balanceX == 0 and balanceY == 0:
            return True
        else:
            return False
