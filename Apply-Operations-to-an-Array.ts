function applyOperations(nums: number[]): number[] {
  const res: number[] = []

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === nums[i + 1]) {
      res.push(nums[i] * 2)
      nums[i + 1] = 0
    } else {
      res.push(nums[i])
    }
  }

  let idx: number = 0

  for (let i = 0; i < res.length; i++) {
    if (res[i] !== 0) {
      res[idx] = res[i]
      idx++
    }
  }

  while (idx < res.length) {
    res[idx] = 0
    idx++
  }

  return res
}