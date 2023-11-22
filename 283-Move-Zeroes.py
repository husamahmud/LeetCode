class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        zero_idx = 0

        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[zero_idx] = nums[zero_idx], nums[i]
                zero_idx += 1
