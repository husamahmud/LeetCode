class Solution(object):
    def characterReplacement(self, s, k):
        counter = [0] * 26
        l = 0
        r = 0
        n = len(s)
        max_count = 0
        max_len = 0

        while r < n:
            # increment the count of the current character
            counter[ord(s[r]) - ord('A')] += 1
            # update the maximum count
            max_count = max(max_count, counter[ord(s[r]) - ord('A')])
            # length of the current window
            window_len = r - l + 1

            # if the number of character changes exceeds the k limit
            if window_len - max_count > k:
                counter[ord(s[l]) - ord('A')] -= 1
                l += 1

            # update the maximum count
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
