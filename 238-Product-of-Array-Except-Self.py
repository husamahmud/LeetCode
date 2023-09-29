class Solution(object):
	def productExceptSelf(self, nums):
		n = len(nums)
		res = [1] * n

		pref = 1
		for i in range(n):
			res[i] *= pref
			pref *= nums[i]

		suff = 1
		for i in range(n - 1, -1, -1):
			res[i] *= suff
			suff *= nums[i]

		return res

	def productExceptSelf(self, nums):
		n = len(nums)
		pref = [1] * n
		suff = [1] * n
		res = [1] * n

		for i in range(1, n):
			pref[i] = nums[i - 1] * pref[i - 1]

		for i in range(n - 2, -1, -1):
			suff[i] = nums[i + 1] * suff[i + 1]

		for i in range(n):
			res[i] = pref[i] * suff[i]

		return res
