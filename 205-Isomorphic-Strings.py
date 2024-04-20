class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        freq = {}
        hashST = {}
        hashTS = {}

        for i in range(n):
            freq[s[i]] = freq.get(s[i], 0) + 1
            hashST[s[i]] = t[i]
            hashTS[t[i]] = s[i]

        for i in range(n):
            if t[i] != hashST[s[i]] or s[i] != hashTS[t[i]] or freq[s[i]] == 0:
                return False
            else:
                freq[s[i]] -= 1
        
        return True