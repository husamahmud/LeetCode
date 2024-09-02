function isAnagram(s: string, t: string): boolean {
  const map = {}

  for (const c of s) {
    if (map[c]) map[c]++
    else map[c] = 1
  }

  for (const c of t) {
    if (map[c]) map[c]--
    else return false
  }

  for (const key in map) if (map[key]) return false
  return true
};