class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;

        dfs(nums, res, subset, 0);

        return res;
    }

private:
    void dfs(vector<int>& nums, vector<vector<int>>& res, vector<int>& subset, int i) {
        if (i == nums.size()) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        dfs(nums, res, subset, i + 1);
        subset.pop_back();
        dfs(nums, res, subset, i + 1);
    }
};