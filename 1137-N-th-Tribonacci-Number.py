class Solution(object):
    def tribonacci(self, n):
        trib = [0, 1, 1]

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        for i in range(3, n + 1):
            trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])

        return trib[-1]
