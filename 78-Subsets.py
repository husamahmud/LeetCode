class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate(subset: List[int], idx: int) -> None:
            res.append(subset[:])

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                generate(subset, i + 1)
                subset.pop()

        generate([], 0)
        return res
