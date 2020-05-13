class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        cnt = 0

        for h in heights:
            count[h] += 1

        j = 0

        for i in range(1, 101):
            # 桶排序
            while count[i] > 0:
                count[i] -= 1

                if heights[j] != i:
                    cnt += 1
                j += 1

        return cnt
