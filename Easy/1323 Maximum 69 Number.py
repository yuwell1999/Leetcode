class Solution:
    def maximum69Number(self, num: int) -> int:
        # replace函数，第三个参数max表示替换最多不超过max次
        return int(str(num).replace('6', '9', 1))
