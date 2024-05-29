class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''.join(word1)
        w2 = ''.join(word2)

        return w1 == w2