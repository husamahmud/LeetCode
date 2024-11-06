function maxProfit(prices: number[]): number {
  let l = 0, r = 1
  let max = 0

  while (r < prices.length) {
    let cur = prices[r] - prices[l]
    max = Math.max(cur, max)

    if (prices[r] >= prices[l]) r++
    else l++
  }

  return max
};