class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        rev_words = [word[::-1] for word in words]

        return ' '.join(rev_words)
