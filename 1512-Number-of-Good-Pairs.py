class Solution(object):
	def numIdenticalPairs(self, nums):
		freq = {}
		count = 0

		for num in nums:
			if num in freq:
				count += freq[num]
				freq[num] += 1
			else:
				freq[num] = 1

		return count
