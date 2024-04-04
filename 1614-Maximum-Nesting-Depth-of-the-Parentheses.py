class Solution:
    def maxDepth(self, s: str) -> int:
        stk = []
        max_depth = 0

        for c in s:
            if c == '(':
                stk.append(c)
            elif c == ')':
                stk.pop()
            max_depth = max(max_depth, len(stk))

        return max_depth
        