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
    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& subset, int i) {
        if (nums.size() == i) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        backtrack(nums, res, subset, i + 1);
        subset.pop_back();

        while (i + 1 < nums.size() && nums[i] == nums[i + 1])
            i++;

        backtrack(nums, res, subset, i + 1);
    }
};