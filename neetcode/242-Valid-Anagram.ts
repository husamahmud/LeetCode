function isAnagram(s: string, t: string): boolean {
  const freq: Record<string, number> = {}

  for (const c of s) {
    freq[c] = (freq[c] || 0) + 1
  }

  for (const c of t) {
    if (!freq[c]) return false
    freq[c]--
  }

  for (const val of Object.values(freq)) {
    if (val !== 0) return false;
  }

  return true
};