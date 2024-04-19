class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j, n = 0, len(nums)

        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j