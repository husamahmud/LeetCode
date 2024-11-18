function lengthOfLongestSubstring(s: string): number {
  const set = new Set<string>()
  let max: number = 0
  let l: number = 0

  for (let r = 0; r < s.length; r++) {
    while (set.has(s[r])) {
      set.delete(s[l])
      l++
    }

    set.add(s[r])
    max = Math.max(max, r - l + 1)
  }

  return max
}