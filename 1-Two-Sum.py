class Solution(object):
    def twoSum(self, nums, target):
        ### Husam
        hash_nums = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_nums:
                return i, hash_nums[diff]
            else:
                hash_nums[num] = i
            
        return -1
