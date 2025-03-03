function pivotArray(nums: number[], pivot: number): number[] {
  const left: number[] = []
  const mid: number[] = []
  const right: number[] = []

  for (const num of nums) {
    if (num < pivot) left.push(num)
    else if (num > pivot) right.push(num)
    else mid.push(num)
  }

  return [...left, ...mid, ...right]
}
