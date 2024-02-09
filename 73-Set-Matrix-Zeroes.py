class Solution(object):
    def setZeroes(self, matrix):
        zero_rows = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0