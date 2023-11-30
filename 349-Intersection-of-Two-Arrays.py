class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return s1.intersection(s2)

    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set()

        for num in nums2:
            if num in s1:
                s2.add(num)

        return s2

    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        freq = {}
        res = []

        for num in s1:
            freq[num] = freq.get(num, 0) + 1

        for num in s2:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            if val >= 2:
                res.append(key)

        return res
