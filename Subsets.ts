function subsets(nums: number[]): number[][] {
  const res: number[][] = []

  const rec = (i: number, ds: number[]): void => {
    if (i === nums.length) {
      res.push([...ds])
      return
    }

    ds.push(nums[i])
    rec(i + 1, ds)

    ds.pop()
    rec(i + 1, ds)
  }

  rec(0, [])
  return res
};