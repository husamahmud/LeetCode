class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        int diff, i;

        for (i = 0; i < nums.size(); i++) {
            diff = target - nums[i];
            if (map.count(diff))
                return {map[diff], i};
            map[nums[i]] = i;
        }

        return {-1};
    }
};