class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        ### solving using backtracking
        def bt(o, c):  ##open, close
            if o == c == n:
                res.append("".join(s))
                return
            if o < n:
                s.append("(")
                ##incremeent open count by1
                bt(o + 1, c)
                s.pop()
            if c < o:
                s.append(')')
                bt(o, c + 1)
                s.pop()

        bt(0, 0)
        return res



