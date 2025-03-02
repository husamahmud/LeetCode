function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
  const res: number[][] = []
  const map: Record<string, number> = {}

  for (const num of nums1) {
    map[num[0]] = num[1]
  }

  for (const num of nums2) {
    if (map[num[0]]) map[num[0]] += num[1]
    else map[num[0]] = num[1]
  }

  Object.entries(map).map(entry => {
    res.push([Number(entry[0]), entry[1]])
  })

  return res
}