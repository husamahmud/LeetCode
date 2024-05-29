class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 1:
            if int(n) == 1:
                return True
            return False

        return self.isPowerOfTwo(n / 2)
