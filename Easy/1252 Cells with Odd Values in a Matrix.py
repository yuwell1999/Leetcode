class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        '''
        :param n:
        :param m:
        :param indices:
        :return:
        '''

        col = [0] * m
        row = [0] * n

        for x, y in indices:
            row[x] += 1
            col[y] += 1

        '''
        # 模拟 + 空间优化
        时间复杂度 L+M*N
        return sum((row[x] + col[y]) % 2 == 1 for x in range(n) for y in range(m))        
        '''

        # 计数 时间复杂度 L+M+N
        '''
        我们可以继续对方法二进行优化。
        可以发现，矩阵中位于 (x, y) 位置的数为奇数，当且仅当 row[x] 和 col[y] 中恰好有一个为奇数, 即只有行或者列进行奇数次增长操作。
        因此对于 row[x] 为偶数，那么在第 x 行有 count_odd(col) 个位置的数为奇数；
        对于 row[x] 为奇数，那么在第 x 行有 m - count_odd(col) 个位置的数为偶数，其中 count_odd(col) 表示数组 col 中奇数的个数。
        将所有的行 x 进行求和，可以得到奇数的数目为 count_odd(row) * (m - count_odd(col)) + (n - count_odd(row)) * count_odd(col)。
        '''
        odd_row = sum(x % 2 == 1 for x in row)
        odd_col = sum(y % 2 == 1 for y in col)

        return odd_row * (m - odd_col) + odd_col * (n - odd_row)  # 奇数乘偶数 加上 偶数乘奇数
