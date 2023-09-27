class Solution(object):
	def shuffle(self, nums, n):
		shuffled = []

		for i in range(n):
			shuffled.append(nums[i])
			shuffled.append(nums[i + n])

		return shuffled
