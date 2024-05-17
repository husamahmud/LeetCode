class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target or \\
                nums[m] > target and nums[m - 1] < target or \\
                nums[m] > target and m == 0:
                return m
            elif nums[m] < target and m == n - 1:
                return m + 1

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
