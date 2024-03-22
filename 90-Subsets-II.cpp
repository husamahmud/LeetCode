class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;

        sort(nums.begin(), nums.end());
        backtrack(nums, res, subset, 0);

        return res;
    }

private:
    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& subset, int idx) {
        res.push_back(subset);

        for (int i = idx; i < nums.size(); i++) {
            if (i > idx && nums[i] == nums[i - 1])
                continue;

            subset.push_back(nums[i]);
            backtrack(nums, res, subset, i + 1);
            subset.pop_back();
        }
    }
};