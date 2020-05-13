class Solution:
    @staticmethod
    def lengthIsEven(n):
        cnt = 0
        while n > 0:
            cnt += 1
            n = int(n / 10)
        return (cnt % 2) == 0

    def findNumbers(self, nums):
        cnt = 0
        for n in nums:
            if Solution.lengthIsEven(n):
                cnt += 1
        return cnt


nums = [555, 901, 482, 1771]
s = Solution()
print(Solution.lengthIsEven(100))
print(s.findNumbers(nums))
