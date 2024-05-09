class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        n, count = len(arr), 0

        if total / k >= threshold:
            count += 1

        for i in range(k, n):
            total = total + arr[i] - arr[i - k]
            if total / k >= threshold:
                count += 1

        return count
