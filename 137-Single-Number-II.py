class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        for i in range(0, len(nums), 3):
            if i + 1 == len(nums) or nums[i] != nums[i + 1]:
                return nums[i]