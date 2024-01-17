class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        values = set()
        for val in freq.values():
            if val in values:
                return False
            values.add(val)

        return True
