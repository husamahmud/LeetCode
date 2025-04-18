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
    rec(i + 1, subset)
  }

  rec(0, [])
  return res
};