class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        for c in s:
            map[c] = map.get(c, 0) + 1

        for c in t:
            if c in map:
                map[c] -= 1
            else:
                return False

        for num in map.values():
            if num != 0:
                return False
        
        return True