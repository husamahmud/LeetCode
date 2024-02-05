class Solution(object):
    def kthSmallest(self, matrix, k):
        arr = []

        for row in matrix:
            arr.extend(row)        

        return sorted(arr)[k - 1]