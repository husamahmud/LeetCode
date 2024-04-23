class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = [entry[0] for entry in sorted(freq.items(), key=lambda x: x[1], reverse=True)]
        
        return res[:k]
