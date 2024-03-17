class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;

        generate(ans, "", n, n);
        return ans;
    }

private:
    void generate(vector<string> &res, string curr, int open, int close) {
        if (open == 0 && close == 0) {
            res.push_back(curr);
            return;
        }

        if (open > 0)
            generate(res, curr + '(', open - 1, close);
        
        if (close > open)
            generate(res, curr + ')', open, close - 1);
    }
};