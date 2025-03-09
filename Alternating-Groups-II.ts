function numberOfAlternatingGroups(colors: number[], k: number): number {
  const n = colors.length
  let l = 0, res = 0

  for (let r = 0; r < n + k - 1; r++) {
    if (colors[r % n] === colors[(r - 1) % n]) l = r
    if (r - l + 1 > k) l++
    if (r - l + 1 === k) res++
  }

  return res
}