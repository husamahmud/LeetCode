function subsetsWithDup(nums: number[]): number[][] {
  const res: number[][] = []
  nums.sort((a, b) => a - b)

  const rec = (i: number, ds: number[]): void => {
    if (i === nums.length) {
      res.push([...ds])
      return
    }

    ds.push(nums[i])
    rec(i + 1, ds)

    while (i + 1 < nums.length && nums[i] === nums[i + 1]) i++

    ds.pop()
    rec(i + 1, ds)
  }

  rec(0, [])
  return res
};