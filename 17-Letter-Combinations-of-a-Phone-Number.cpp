class Solution {
public:
	vector <string> letterCombinations(string digits) {
		if (digits.empty()) {
			return {};
		}

		vector <string> res;
		unordered_map<char, string> phoneMap = {{'2', "abc"},
		                                        {'3', "def"},
		                                        {'4', "ghi"},
		                                        {'5', "jkl"},
		                                        {'6', "mno"},
		                                        {'7', "pqrs"},
		                                        {'8', "tuv"},
		                                        {'9', "wxyz"}};

		backtrack(res, "", digits, phoneMap, 0);
		return res;
	}

private:
	void
	backtrack(vector <string> &res, string comb, string digits, unordered_map<char, string> &phoneMap, int idx) {
		if (idx == digits.length()) {
			res.push_back(comb);
			return;
		}

		char digit = digits[idx];
		string letters = phoneMap[digit];

		for (char letter: letters) {
			backtrack(res, comb + letter, digits, phoneMap, idx + 1);
		}
	}
};