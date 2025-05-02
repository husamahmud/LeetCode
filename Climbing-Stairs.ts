function climbStairs(n: number): number {
  const noOfWays: number[] = new Array(n + 1).fill(1)

  for (let i = 2; i < n + 1; i++) {
    noOfWays[i] = noOfWays[i - 1] + noOfWays[i - 2]
  }

  return noOfWays.at(-1)
};