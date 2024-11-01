function threeSum(nums: number[]): number[][] {
  const n: number = nums.length
  let res: number[][] = []
  let l: number, r: number

  nums.sort((a: number, b: number) => a - b)

  for (let i = 0; i < n - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue

    l = i + 1, r = n - 1
    while (l < r) {
      const threeSum = nums[i] + nums[l] + nums[r]

      if (threeSum < 0) {
        l++
      } else if (threeSum > 0) {
        r--
      } else {
        res.push([nums[i], nums[l], nums[r]])
        l++, r--

        while (l < r && nums[l] === nums[l - 1]) l++
      }
    }
  }

  return res
}; 