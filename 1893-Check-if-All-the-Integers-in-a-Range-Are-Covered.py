class Solution(object):
	def isCovered(self, ranges, left, right):
		covered = set()

		for start, end in ranges:
			for num in range(start, end + 1):
				covered.add(num)

		for num in range(left, right + 1):
			if num not in covered:
				return False

		return True
