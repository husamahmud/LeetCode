class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        res = set()

        for i in range(1, n + 1):
            if i not in nums:
                res.add(i)

        return res

