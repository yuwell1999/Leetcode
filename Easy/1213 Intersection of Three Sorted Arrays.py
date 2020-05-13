class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

        # minV = min(arr1[0],arr2[0],arr3[0])
        # maxV = max(arr1[-1],arr2[-1],arr3[-1])
        # list = []
        # for i in range(minV,maxV+1):
        #     if i in arr1 and i in arr2 and i in arr3:
        #         list.append(i)
        #
        # return list

        # 使用集合方法
        s = arr1 + arr2 + arr3
        list = []
        for i in set(s):
            if s.count(i) == 3:
                list.append(i)
        return list
