class Solution(object):
	def twoSum(self, numbers, target):
		l = 0
		r = len(numbers) - 1

		while l < r:
			if numbers[r] + numbers[l] > target:
				r -= 1
			elif numbers[r] + numbers[l] < target:
				l += 1
			else:
				return [l + 1, r + 1]
