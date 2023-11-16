class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        hash_s = {}
        n = len(s)
        for i in range(n):
            char_s = s[i]
            char_t = t[i]

            if char_s in hash_s and hash_s[char_s] != char_t:
                return False
            elif char_s not in hash_s and char_t in hash_s.values():
                return False
            hash_s[char_s] = char_t

        return True
