# Bayor-Moore vote
class Solution:
    @staticmethod
    def majorityElement(nums):
        '''
        :param nums: List[int]
        :return: int
        '''
        major = count = 0

        for i in nums:
            if count == 0:
                major = i

            if i == major:
                count += 1
            else:
                count -= 1

        return major


num = [int(n) for n in input().split()]
print(Solution.majorityElement(num))
