class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        stk = []

        for i in range(n):
            c = s[i]
            if stk and c.lower() == stk[-1].lower() and c != stk[-1]:
                stk.pop()
            else:
                stk.append(c)

        return "".join(stk)