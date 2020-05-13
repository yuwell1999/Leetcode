import numpy as np


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        lst = []
        for i in range(1, np.power(10, n)):
            # print(i," ",end="")
            lst.append(i)
        # print(np.power(10,n)-1,end="")
        return lst
