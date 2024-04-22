class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        
        freqS1 = Counter(s1)
        window = {}
        l = 0

        for r in range(n2):
            right = s2[r]
            window[right] = window.get(right, 0) + 1

            if r - l + 1 == n1:
                if window == freqS1:
                    return True
                
                left = s2[l]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
                
                l += 1

        return False