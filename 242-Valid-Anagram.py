class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = Counter(s)

        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1

        return True