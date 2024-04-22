class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count("b")
        a = text.count("a")
        l = text.count("l") // 2
        o = text.count("o") // 2
        n = text.count("n")

        return min(b, a, l, o, n)
