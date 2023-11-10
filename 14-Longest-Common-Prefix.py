class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs is None:
            return None

        strs.sort()

        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break

        return prefix
