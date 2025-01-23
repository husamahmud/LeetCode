function intersection(nums1: number[], nums2: number[]): number[] {
  const res: number[] = []
  const set = new Set<number>(nums1)

  for (const num of nums2) {
    if (set.has(num)) {
      res.push(num)
      set.delete(num)
    }
  }

  return res
};