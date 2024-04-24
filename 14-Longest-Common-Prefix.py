class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = \\
        sortedStrs = sorted(strs, key=str.lower)
        smallest = sortedStrs[0]
        longest = sortedStrs[-1]

        for i in range(len(smallest)):
            if smallest[i] == longest[i]:
                pre += smallest[i]
            else:
                return pre

        return pre
        