class Solution:
    def isValid(self, s: str) -> bool:
        m = {'}':'{', ']':'[', ')':'('}
        stack = []

        for c in s:
            if c not in m:
                stack.append(c)
            elif c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return not stack