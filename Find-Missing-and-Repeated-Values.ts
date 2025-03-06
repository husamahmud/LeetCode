function findMissingAndRepeatedValues(grid: number[][]): number[] {
  const map: Record<string, number> = {}
  const n: number = grid.length
  let missing = 0, repeated = 0

  for (let i = 1; i <= n * n; i++) map[i] = 0

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      map[grid[i][j]]++
    }
  }

  Object.entries(map).forEach(entry => {
    const key = Number(entry[0])
    const count = entry[1]

    if (count === 0) missing = key
    if (count > 1) repeated = key
  })

  return [repeated, missing]
}