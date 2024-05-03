class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        p1 = p2 = 0

        while p1 < len(word1) and p2 < len(word2):
            word += word1[p1]
            word += word2[p2]
            p1 += 1
            p2 += 1

        if p1 < len(word1):
            word += word1[p1:]

        if p2 < len(word2):
            word += word2[p2:]

        return word
