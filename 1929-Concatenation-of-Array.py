class Solution(object):
	def getConcatenation(self, nums):
		# 1
		nums.extend(nums)
		return nums
		# 2
		return nums + nums
		# 3
		return [*nums, *nums]
		# 4
		ans = []
		for i in range(2):
			for num in nums:
				ans.append(num)
		return ans
