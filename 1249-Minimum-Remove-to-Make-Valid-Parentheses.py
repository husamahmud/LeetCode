class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = ""
        stack = []
        opened = 0
        closed = 0

        for char in s:
            if char == "(":
                opened += 1
            elif char == ")":
                closed += 1
            if closed > opened:
                closed -= 1
            else:
                stack.append(char)

        while stack:
            char = stack.pop()
            if opened > closed and char == "(":
                opened -= 1
            else:
                result += char

        return result[::-1]
