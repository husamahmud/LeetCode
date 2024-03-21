class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> curr;

        sort(nums.begin(), nums.end());
        backtrack(nums, res, curr, 0);

        return res;
    }

private:
    void backtrack(vector<int>& nums, vector<vector<int>>& res, vector<int>& curr, int idx) {
        res.push_back(curr);

        for (int i = idx; i < nums.size(); i++) {
            if (i > idx && nums[i] == nums[i - 1])
                continue;

            curr.push_back(nums[i]);
            backtrack(nums, res, curr, i + 1);
            curr.pop_back();
        }
    }
};