if __name__ == '__main__':
	s = ["h", "e", "l", "l", "o"]
	l = 0
	r = len(s) - 1

	while l < r:
		temp = s[l]
		s[l] = s[r]
		s[r] = temp
		l += 1
		r -= 1

	print(s)
