class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = j = 0

        while i < len(nums1):
            j = nums2.index(nums1[i])
            found = False

            while j < len(nums2):
                if nums1[i] < nums2[j]:
                    res.append(nums2[j])
                    found = True
                    break
                j += 1
            
            if not found:
                res.append(-1)
            
            i += 1

        return res
