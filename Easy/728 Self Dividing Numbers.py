class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def canbeDivided(n):
            for i in str(n):
                if i == '0' or n % int(i) > 0:
                    return False

            return True

        list = []

        for i in range(left, right + 1):
            if canbeDivided(i):
                list.append(i)

        return list
