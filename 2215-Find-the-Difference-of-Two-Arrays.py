class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []
        dif = set()

        for num in nums1:
            if num not in nums2:
                dif.add(num)
        res.append(list(dif))

        dif.clear()

        for num in nums2:
            if num not in nums1:
                dif.add(num)
        res.append(list(dif))

        return res

