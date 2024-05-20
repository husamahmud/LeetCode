class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            m = l + (r - l) // 2
            num = guess(m)

            if num == 0:
                return m
            elif num == 1:
                l = m + 1
            else:
                r = m - 1