class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2
            num = matrix[m // cols][m % cols]

            if num < target:
                l = m + 1
            elif num > target:
                r = m - 1
            else:
                return True

        return False
