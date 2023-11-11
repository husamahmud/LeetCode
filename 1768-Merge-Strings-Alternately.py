class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        n1 = len(word1)
        n2 = len(word2)
        i = j = 0

        while i < n1 or j < n2:
            if i < n1:
                res += word1[i]
                i += 1
            if j < n2:
                res += word2[j]
                j += 1

        return res
