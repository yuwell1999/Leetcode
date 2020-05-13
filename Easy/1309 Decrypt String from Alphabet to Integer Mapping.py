class Solution:
    def freqAlphabest(self, s: str) -> str:
        def toASCII(st):
            return chr(int(st) + 96)

        i, list = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                list += toASCII(s[i:i + 2])
                i += 2
            else:
                list += toASCII(s[i])

            i += 1
        return list
