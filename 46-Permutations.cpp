class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> perm = nums;

        bt(nums, res, perm, 0);

        return res;
    }

private:
    void bt(vector<int>& nums, vector<vector<int>>& res, vector<int>& perm, int i) {
        if (i == nums.size()) {
            res.push_back(perm);
            return;
        }

        for (int j = i; j < nums.size(); j++) {
            swap(perm[j], perm[i]);
            bt(nums, res, perm, i + 1);
            swap(perm[j], perm[i]);
        }
    }
};