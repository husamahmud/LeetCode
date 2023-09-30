class Solution(object):
	def isValidSudoku(slef, board):
		# check rows
		for i in range(9):
			row_nums = set()
			for j in range(9):
				cell = board[i][j]
				if cell != '.':
					if cell in row_nums:
						return False
					else:
						row_nums.add(cell)

		# check columns
		for j in range(9):
			col_nums = set()
			for i in range(9):
				cell = board[i][j]
				if cell != '.':
					if cell in col_nums:
						return False
					else:
						col_nums.add(cell)

		# check 3x3 sub-boxes
		for box in range(9):
			box_nums = set()
			for i in range(box // 3 * 3, box // 3 * 3 + 3):
				for j in range(box % 3 * 3, box % 3 * 3 + 3):
					cell = board[i][j]
					if cell != '.':
						if cell in box_nums:
							return False
						else:
							box_nums.add(cell)

		return True
