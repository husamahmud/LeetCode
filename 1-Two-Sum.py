class Solution(object):
	def twoSum(self, nums, target):
		hash_nums = {}

		for i, num in enumerate(nums):
			diff = target - num
			if diff in hash_nums:
				return [hash_nums[diff], i]
			else:
				hash_nums[num] = i
