class Solution(object):
	def isHappy(self, n):
		visited = set()
		while n not in visited:
			visited.add(n)
			n = self.sumOfSquares(n)
			if n == 1:
				return True
		return False

	def sumOfSquares(self, n):
		res = 0
		while n != 0:
			res += (n % 10) ** 2
			n //= 10
		return res
