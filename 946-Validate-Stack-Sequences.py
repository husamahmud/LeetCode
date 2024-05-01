class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0

        while j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                if i >= len(pushed):
                    break
                stack.append(pushed[i])
                i += 1

        return len(stack) == 0