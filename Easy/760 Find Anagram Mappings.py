class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        lst = []
        for n in A:
            lst.append(B.index(n))
        return lst
