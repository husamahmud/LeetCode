class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        n = len(nums)

        for i in range(n):
            diff = target - nums[i]
            if diff in hash:
                return hash[diff], i
            else:
                hash[nums[i]] = i

        return -1