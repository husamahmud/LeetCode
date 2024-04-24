class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for i in reversed(range(n)):
            swapped = False
            for j in range(i):
                if nums[j] > nums[j + 1]:
                    swapped = True
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if not swapped:
                break
                