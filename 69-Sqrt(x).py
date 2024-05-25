class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = l + (r - l) // 2

            if m**2 == x:
                return m
            elif m**2 > x:
                r = m - 1
            else:
                l = m + 1

        return r