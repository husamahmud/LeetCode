function productExceptSelf(nums: number[]): number[] {
  const n: number = nums.length
  const pref: number[] = new Array(n).fill(1)
  const suff: number[] = new Array(n).fill(1)
  const res: number[] = new Array(n).fill(1)

  for (let i = 1; i < n; i++) {
    pref[i] = pref[i - 1] * nums[i - 1]
  }

  for (let i = n - 2; i >= 0; i--) {
    suff[i] = suff[i + 1] * nums[i + 1]
  }

  for (let i = 0; i < n; i++) {
    res[i] = suff[i] * pref[i]
  }

  return res
};