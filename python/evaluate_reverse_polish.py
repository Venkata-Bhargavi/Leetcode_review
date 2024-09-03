class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                a = s.pop()
                b = s.pop()

                if i == "+":
                    s.append(int(a) + int(b))
                elif i == "-":
                    s.append(int(b) - int(a))
                elif i == "*":
                    s.append(int(b) * int(a))
                elif i == "/":
                    s.append(int(b / a))
            else:
                s.append(int(i))

        return s[0]



