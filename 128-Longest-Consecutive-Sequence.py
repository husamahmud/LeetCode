class Solution(object):
	def longestConsecutive(self, nums):
		nums_set = set(nums)
		res = 0

		for num in nums_set:
			if num - 1 not in nums_set:
				curr = num
				count = 1
				while curr + 1 in nums_set:
					curr += 1
					count += 1
				res = max(res, count)

		return res

	def longestConsecutive(self, nums):
		uniq = sorted(set(nums))
		n = len(uniq)
		count = 0
		res = 0

		for i in range(n):
			if i > 0 and uniq[i] == uniq[i - 1] + 1:
				count += 1
			else:
				count = 1
			res = max(res, count)

		return res
