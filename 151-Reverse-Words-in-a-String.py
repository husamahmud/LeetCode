class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        return ' '.join(reversed(words))
