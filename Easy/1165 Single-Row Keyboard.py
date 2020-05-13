import numpy as np


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        step = 0
        cur = 0
        for i in word:
            step += np.abs(cur - keyboard.index(i))
            cur = keyboard.index(i)
        return step
