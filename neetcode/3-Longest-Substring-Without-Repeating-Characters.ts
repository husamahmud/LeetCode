function lengthOfLongestSubstring(s: string): number {
  const map = new Map<string, number>()
  let max: number = 0
  let start: number = 0

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i])) {
      start = Math.max(start, map.get(s[i]) + 1)
    }

    map.set(s[i], i)
    max = Math.max(max, i - start + 1)
  }

  return max
};