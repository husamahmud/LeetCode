class Solution(object):
    def merge_two_arr(self, nums1, nums2):
        nums = [0] * (len(nums1) + len(nums2))
        i = j = 0
        while len(nums1) > i and len(nums2) > j:
            if nums1[i] < nums2[j]:
                nums[i + j] = nums1[i]
                i += 1
            else:
                nums[i + j] = nums2[j]
                j += 1
        while len(nums1) > i:
            nums[i + j] = nums1[i]
            i += 1
        while len(nums2) > j:
            nums[i + j] = nums2[j]
            j += 1
        return nums, len(nums)

    def findMedianSortedArrays(self, nums1, nums2):
        nums, n = self.merge_two_arr(nums1, nums2)
        if n % 2 != 0:
            return nums[n // 2]
        else:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2.0