class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}

        for i, num in enumerate(nums):
            if num in m and abs(m[num] - i) <= k:
                return True
            else:
                m[num] = i

        return False
        
