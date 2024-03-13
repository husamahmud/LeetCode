class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> pq;
        unordered_map<int, int> mp;
        vector<int> ans;

        for (int num : nums)
            mp[num]++;

        for (auto entry : mp)
            pq.push({entry.second, entry.first});

        while (k--) {
            ans.push_back(pq.top().second);
            pq.pop();
        }

        return (ans);
    }
};