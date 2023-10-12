class Solution(object):
    def lengthOfLastWord(self, s):
        splited = s.split()
        return len(splited[-1])
