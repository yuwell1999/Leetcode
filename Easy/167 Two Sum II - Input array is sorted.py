class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s_index = 0
        b_index = len(numbers) - 1

        while s_index < b_index:
            if numbers[s_index] + numbers[b_index] == target:
                return [s_index + 1, b_index + 1]
            if numbers[s_index] + numbers[b_index] > target:  # 两数之和大于target，需要减小值
                b_index -= 1
            if numbers[s_index] + numbers[b_index] < target:  # 两数之和小于target，需要增加值
                s_index += 1
