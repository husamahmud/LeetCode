class Solution(object):
	def countPairs(self, nums, target):
		nums.sort()
		l = 0
		r = len(nums) - 1
		count = 0

		while l < r:
			if nums[r] + nums[l] < target:
				count += r - l
				l += 1
			else:
				r -= 1

		return count
