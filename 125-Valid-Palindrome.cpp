class Solution {
public:
    bool isPalindrome(string s) {
        int r = 0, l = s.size() - 1;

        while (r < l) {
            if (!isalnum(s[r])) {
                r++;
                continue;
            }

            if (!isalnum(s[l])) {
                l--;
                continue;
            }

            if ((char)tolower(s[r]) != (char)tolower(s[l]))
                return false;

            r++, l--;
        }

        return true;
    }
};