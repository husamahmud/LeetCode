function subsets(nums: number[]): number[][] {
  const res: number[][] = []

  const rec = (i: number, subset: number[]): void => {
    if (i === nums.length) {
      res.push([...subset])
      return
    }

    subset.push(nums[i])
    rec(i + 1, subset)
    subset.pop()

    while (i + 1 < nums.length && nums[i] === nums[i + 1]) continue
    rec(i + 1, subset)
  }

  rec(0, [])
  return res
};