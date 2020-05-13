class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        cnt = 0
        for i in range(0, 3):
            if guess[i] == answer[i]:
                cnt += 1
        return cnt
