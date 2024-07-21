function productExceptSelf(nums: number[]): number[] {
  const len = nums.length
  const pre = new Array(len).fill(1)
  const suf = new Array(len).fill(1)
  const res = new Array(len).fill(1)

  for (let i = 1; i < len; i++) {
    pre[i] = pre[i - 1] * nums[i - 1]
  }

  for (let i = len - 2; i >= 0; i--) {
    suf[i] = suf[i + 1] * nums[i + 1]
  }

  for (let i = 0; i < len; i++) {
    res[i] = suf[i] * pre[i]
  }

  return res
};