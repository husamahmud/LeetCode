class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram;
        string sorted_str;
        vector<vector<string>> res;

        for (string str : strs) {
            sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            anagram[sorted_str].push_back(str);
        }

        for (const auto entry : anagram)
            res.push_back(entry.second);

        return (res);
    }
};