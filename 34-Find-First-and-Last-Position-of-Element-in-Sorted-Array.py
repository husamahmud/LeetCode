class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                first = m
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if first == -1:
            return [-1, -1]

        l = first
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                last = m
                l = m + 1
            else:
                r = m - 1

        return [first, last]
