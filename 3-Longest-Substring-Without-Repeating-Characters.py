class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        l = 0
        r = 0
        max_len = 0
        substrings = set()

        while r < len(s):
            if s[r] not in substrings:
                substrings.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                substrings.remove(s[l])
                l += 1

        return max_len


if __name__ == '__main__':
    s = "dvdf"
    if not s:
        print()
    l = 0
    r = 1
    substrings = set()
    substrings.add(s[0])
    n = 1
    max_len = 1

    while r < len(s):
        if s[r] in substrings:
            l = r
            n = 1
        else:
            substrings.add(s[r])
            n += 1
            max_len = max(max_len, n)
        r += 1

    print(max_len)
