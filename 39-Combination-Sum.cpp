class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> comb;

        bt(candidates, res, comb, target, 0);
        return res;
    }

private:
    int sum(vector<int> nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); i++)
            res += nums[i];
        return res;
    }

    void bt(vector<int> candidates, vector<vector<int>>& res, vector<int>& comb, int target, int i) {
        if (sum(comb) == target) {
            res.push_back(comb);
            return;
        }

        if (i >= candidates.size() || sum(comb) > target)
            return;

        comb.push_back(candidates[i]);
        bt(candidates, res, comb, target, i);
        comb.pop_back();
        bt(candidates, res, comb, target, i + 1);
    }
};