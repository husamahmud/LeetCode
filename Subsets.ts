function subsets(nums: number[]): number[][] {
  const res: number[][] = []
  const n: number = nums.length

  function fn(i: number, subset: number[]): void {
    if (i >= n) {
      res.push([...subset])
      return
    }

    subset.push(nums[i])
    fn(i + 1, subset)
    subset.pop()
    fn(i + 1, subset)
  }

  fn(0, [])
  return res
}