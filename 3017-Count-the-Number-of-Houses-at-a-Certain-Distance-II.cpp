class Solution {
public:
    vector<long long> countOfPairs(int n, int x, int y) {
    if (y < x) swap(x, y);

    vector<long long> ans(n);
    int cycle = y - x + 1, halfCycle = cycle - 1 >> 1, tail1 = x - 1, tail2 = n - y;
    int tailToTail = tail1 + tail2 + 1 + (x != y);

    // in the cycle
    for (int i = 0; i < halfCycle; i++)
        ans[i] = cycle * 2;
    if (cycle % 2 == 0)
        ans[halfCycle] = cycle;

    // tail to tail
    for (int i = 1; i < tailToTail; i++)
        ans[i - 1] += (tailToTail - i) * 2;
    if (x != y) {
        ans[0] -= 2;
        for (int tail : {tail1, tail2})
            for (int i = 1; i <= tail; i++)
                ans[i] -= 2;
    }

    // tails to the cycle
    for (int tail : {tail1, tail2}) {
        for (int i = 1; i < tail + halfCycle; i++)
            ans[i] += 4 * min({tail, halfCycle, i, tail + halfCycle - i});
        if (cycle % 2 == 0)
            for (int i = 1; i <= tail; i++)
                ans[i + halfCycle] += 2;
    }

    return ans;
}
};