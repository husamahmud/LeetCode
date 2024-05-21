class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> subset;

        bt(nums, res, subset, 0);
        return res;
    }

private:
    void bt(vector<int> nums, vector<vector<int>>& res, vector<int>& subset,
            int i) {
        if (nums.size() == i) {
            res.push_back(subset);
            return;
        }

        subset.push_back(nums[i]);
        bt(nums, res, subset, i + 1);
        subset.pop_back();
        bt(nums, res, subset, i + 1);
    }
};