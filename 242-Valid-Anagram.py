class Solution(object):
	def isAnagram(self, s, t):
		hash_s = {}
		hash_t = {}

		if len(s) != len(t):
			return False

		for c in s:
			if c in hash_s:
				hash_s[c] += 1
			else:
				hash_s[c] = 1

		for c in t:
			if c in hash_t:
				hash_t[c] += 1
			else:
				hash_t[c] = 1

		return hash_s == hash_t
