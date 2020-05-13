class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        sum = 0
        cur = col - 1

        for n in grid:
            for i in range(cur, -1, -1):
                if n[i] >= 0:
                    if i + 1 < col:
                        cur = i + 1
                        sum += col - cur
                    break
            if i == 0 and n[0] < 0:  # 统计最后一行
                sum += col
        return sum
