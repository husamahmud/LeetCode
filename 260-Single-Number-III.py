class Solution(object):
    def singleNumber(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []
        for num, count in freq.items():
            if count == 1:
                res . append(num)

        return res 
        