class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        row = [1]
        res = self.generate(numRows - 1)
        last_row = res[-1]

        for i in range(len(last_row) - 1):
            row.append(last_row[i] + last_row[i + 1])

        row += [1]
        res.append(row)

        return res