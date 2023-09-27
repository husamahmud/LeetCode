class Solution(object):
	def groupAnagrams(self, strs):
		hash_strs = {}
		res = []

		for str in strs:
			sorted_str = tuple(sorted(str))
			if sorted_str in hash_strs:
				hash_strs[sorted_str] += [str]
			else:
				hash_strs[sorted_str] = [str]

		for str in hash_strs.values():
			res.append(str)

		return res
