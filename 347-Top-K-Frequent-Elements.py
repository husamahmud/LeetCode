class Solution(object):
	def topKFrequent(self, nums, k):
		freq = {}
		res = []

		# count the frequency of each number in the nums list
		for num in nums:
			freq[num] = freq.get(num, 0) + 1

		# sort the freq dic by its values
		sorted_hash = sorted(freq.items(), key=lambda x: x[1], reverse=True)

		# Append only the key
		for i in range(k):
			res.append(sorted_hash[i][0])

		return res
