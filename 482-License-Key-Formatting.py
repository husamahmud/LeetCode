class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '')
        group = len(s) % k
        grouping = []

        if group:
            grouping.append(s[:group])

        for idx in range(group, len(s), k):
            grouping.append(s[idx: idx + k])

        return '-'.join(grouping).upper()
