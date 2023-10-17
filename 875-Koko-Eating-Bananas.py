class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)

        while l <= r:
            m = (r + l) // 2
            hours = self.calcHours(piles, m)
            if hours <= h:
                r = m - 1
            else:
                l = m + 1

        return l

    def calcHours(self, piles, k):
        hours = 0
        for bananas in piles:
            hours += (bananas + k - 1) // k
        return hours
