class Solution:
    def toLowerCase(self, str: str) -> str:
        newStr = ""

        for i in str:
            if 'A' <= i <= 'Z':
                # chr函数返回字符
                # ord函数返回ASCII值
                i = chr(ord(i) + 32)

            newStr += i

        return newStr
