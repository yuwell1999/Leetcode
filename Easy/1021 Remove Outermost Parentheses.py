class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        s = ''

        for i in S:
            if i == '(':
                stack.append(i)
                if len(stack) > 1:
                    s += '('
            else:
                stack.pop()
                if len(stack) != 0:
                    s += ')'

        return s
