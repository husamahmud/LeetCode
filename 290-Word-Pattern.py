class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern, s = list(pattern), s.split(' ')

        if len(pattern) != len(s):
            return False

        hashPS, hashSP = {}, {}

        for i in range(len(s)):
            if pattern[i] in hashPS and hashPS[pattern[i]] != s[i]:
                return False
            hashPS[pattern[i]] = s[i]

            if s[i] in hashSP and hashSP[s[i]] != pattern[i]:
                return False
            hashSP[s[i]] = pattern[i]

        return True
        


