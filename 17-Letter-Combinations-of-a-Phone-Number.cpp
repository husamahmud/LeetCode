class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty())
            return {};

        vector<string> res;
        unordered_map<char, string> phoneMap = {
            {'2', "abc"}, {'3', "def"},  {'4', "ghi"}, {'5', "jkl"},
            {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};

        bt(res, "", digits, phoneMap, 0);
        return res;
    }

private:
    void bt(vector<string>& res, string comb, string digits,
            unordered_map<char, string>& phoneMap, int i) {
        if (i == digits.length()) {
            res.push_back(comb);
            return;
        }

        char digit = digits[i];
        string letters = phoneMap[digit];

        for (char letter : letters)
            bt(res, comb + letter, digits, phoneMap, i + 1);
    }
};