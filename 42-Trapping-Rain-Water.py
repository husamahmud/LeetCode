class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        minHeight = [0] * n
        h = 0

        for i in range(n):
            maxLeft[i] = h
            if h < height[i]:
                h = height[i]

        h = 0
        for i in range(n)[::-1]:
            maxRight[i] = h
            if h < height[i]:
                h = height[i]

        for i in range(n):
            minHeight[i] = min(maxLeft[i], maxRight[i])

        result = 0
        for i in range(n):
            water = minHeight[i] - height[i]
            if water > 0:
                result += water

        return result