class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        :param nums:
        :param target:
        :return:
        '''

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:  # 在右侧区间匹配target
                left = mid + 1
            else:  # 在左侧区间匹配target
                right = mid - 1

        return left
