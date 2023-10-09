class Solution(object):
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        s1_freq = {}
        window_freq = {}
        left = right = 0

        # If s1 is longer than s2, return False
        if n1 > n2:
            return False

        # count the freq of chars in s1 and store it in s1_freq
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1

        # slide the window through s2
        while right < n2:
            # add the currnet char to the window_freq
            window_freq[s2[right]] = window_freq.get(s2[right], 0) + 1

            # if the window size is equal to s1's  size
            if right - left + 1 == n1:
                if window_freq == s1_freq:
                    return True

                # shrink the window by moving the left pointer
                window_freq[s2[left]] -= 1
                # if the freq of the current char become zero remove it from the dict
                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]
                left += 1

            right += 1
        # if no premutation found, then return False
        return False
