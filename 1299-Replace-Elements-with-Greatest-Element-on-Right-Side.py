class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        max = -1

        for i in range(n - 1, -1, -1):
            res[i] = max
            if arr[i] > max:
                max = arr[i]

        return res