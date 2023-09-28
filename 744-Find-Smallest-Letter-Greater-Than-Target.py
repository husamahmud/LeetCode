if __name__ == '__main__':
	letters = ["c", "f", "j"]
	target = 'a'

	target_ascii = ord(target)
	left = 0
	right = len(letters)
	res = ''

	while left <= right:
		mid = (left + right) // 2

		if ord(letters[mid]) > target_ascii:
			res = letters[mid]
			right = mid - 1
		else:
			left = mid + 1

	print(res)
