class Solution(object):
	def containsDuplicate(self, nums):
		unique_nums = set()

		for i in range(len(nums)):
			if nums[i] in unique_nums:
				return True
			unique_nums.add(nums[i])
		return False

	def containsDuplicate(self, nums):
		return len(set(nums)) != len(nums)
