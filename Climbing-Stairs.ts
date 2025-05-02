function climbStairs(n: number): number {
  const dp: number[] = new Array(n + 1).fill(1)

  for (let i = 2; i < n + 1; i++) dp[i] = dp[i - 1] + dp[i - 2]

  return dp.at(-1)
};