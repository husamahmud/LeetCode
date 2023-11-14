class Solution(object):
    def wordPattern(self, pattern, s):
        s_list = s.split(' ')

        if len(pattern) != len(s_list):
            return False

        pattern_d = {}
        word_d = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = s_list[i]

            if char not in pattern_d:
                pattern_d[char] = word
            elif pattern_d[char] != word:
                return False

            if word not in word_d:
                word_d[word] = char
            elif word_d[word] != char:
                return False

        return True
