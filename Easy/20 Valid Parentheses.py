class Solution(object):
    def isValid(self, s):
        stack = []
        # 右括号匹配左括号
        map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for i in s:
            # 不属于右括号匹配左括号，当前符号进栈
            if i not in map:
                stack.append(i)

            # 匹配成功，弹出栈
            else:
                if stack:
                    top = stack.pop()
                else:
                    top = '$'

                if map[i] != top:
                    return False

        return not stack
