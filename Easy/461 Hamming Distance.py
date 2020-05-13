class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dis = 0
        xor = x ^ y

        '''
        移位操作

        # 右移操作
        while xor:
            # 检查最后一位是否为1
            if xor & 1:
                dis += 1

            xor >>= 1

        return dis
        '''

        # Brian.Kernighan
        # 当我们在 number 和 number-1 上做 AND 位运算时，原数字 number 的最右边等于 1 的比特会被移除。
        '''
        x       = 1000 1000 
        x-1     = 1000 0111
        x&(x-1) = 1000 0000
        '''
        while xor:
            dis += 1
            xor = xor & (xor - 1)
        return dis
