class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1 : r + 1]
                skip_right = s[l:r]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

            l, r = l + 1, r - 1

        return True
