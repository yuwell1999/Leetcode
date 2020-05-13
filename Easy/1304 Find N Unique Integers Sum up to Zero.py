class Solution:
    def sumZero(self, n: int) -> List[int]:
        # n-1个数放入数组，和为sum，剩下的一个数和为-sum
        list = [x for x in range(n - 1)]
        list.append(-1 * sum(list))
        return list
