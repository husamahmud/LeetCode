class Solution(object):
	def finalValueAfterOperations(self, operations):
		res = 0

		for op in operations:
			if op[0] == '-' or op[2] == '-':
				res -= 1
			else:
				res += 1

		return res
