class Solution(object):
    def isPowerOfTwo(self, n):
        if n < 1:
            return False
        elif n == 1:
            return True
        elif n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)
