class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(0, len(nums), 2):
            temp = []
            for j in range(0, nums[i]):
                temp.append(nums[i + 1])
            lst += temp
        return lst
