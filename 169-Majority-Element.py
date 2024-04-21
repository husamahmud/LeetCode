class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        curMax = 0
        maj = None

        for num in freq:
            if curMax < freq[num]:
                curMax = freq[num]
                maj = num
        
        return maj