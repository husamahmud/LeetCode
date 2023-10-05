class Solution(object):
    def maxArea(self, height):
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            # calculate the area
            area = (r - l) * min(height[l], height[r])
            # update the maximum area
            max_area = max(max_area, area)
            # move the pointer that points to the shorter line
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
