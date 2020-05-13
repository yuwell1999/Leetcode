class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        :param arr:
        :return lst:
        '''
        lst = [0] * (len(arr) - 1) + [-1]
        # 逆序遍历
        for i in range(len(arr) - 2, -1, -1):
            lst[i] = max(lst[i + 1], arr[i + 1])

        return lst
