function combinationSum2(candidates: number[], target: number): number[][] {
  const res = new Set<number[]>()
  candidates.sort((a, b) => a - b)

  const fn = (i: number, t: number, comb: number[]) => {
    if (t === 0) {
      res.add([...comb])
      return
    }

    if (i >= candidates.length || t < 0) return

    if (candidates[i] <= t) {
      comb.push(candidates[i])
      fn(i + 1, t - candidates[i], comb)
      comb.pop()
    }

    while (i + 1 < candidates.length && candidates[i] === candidates[i + 1]) i++

    fn(i + 1, t, comb)
  }

  fn(0, target, [])
  return Array.from(res)
};