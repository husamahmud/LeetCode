class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int], l: int, r: int) -> int:
            if l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    return binarySearch(nums, m + 1, r)
                elif nums[m] > target:
                    return binarySearch(nums, l, m - 1)
                else:
                    return m
            else:
                return -1

        return binarySearch(nums, 0, len(nums) - 1)
