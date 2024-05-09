class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)

        i = float(\inf\)
        j = float(\inf\)

        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True

        return False
