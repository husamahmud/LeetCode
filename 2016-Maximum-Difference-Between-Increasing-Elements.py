class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        i, j = 0, 1
        maxDif = 0

        while j < len(nums):
            if nums[i] < nums[j]:
                curDif = nums[j] - nums[i]
                maxDif = max(maxDif, curDif)
            else:
                i = j
            j += 1

        return maxDif if maxDif > 0 else -1
