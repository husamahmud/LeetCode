class Solution(object):
	def buildArray(self, nums):
		n = len(nums)
		res = [0] * n

		for i in range(n):
			res[i] = nums[nums[i]]

		return res
