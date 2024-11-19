function mapsAreEqual(map1, map2) {
  if (map1.size !== map2.size) return false;
  for (const [key, val] of map1) {
    if (map2.get(key) !== val) return false;
  }
  return true;
}


function checkInclusion(s1: string, s2: string): boolean {
  const n1: number = s1.length, n2: number = s2.length
  if (n1 > n2) return false

  let m1 = new Map()
  let m2 = new Map()
  let l: number = 0

  for (const c of s1) m1.set(c, (m1.get(c) || 0) + 1);

  for (let r = 0; r < n2; r++) {
    m2.set(s2[r], (m2.get(s2[r]) || 0) + 1);

    if (r - l + 1 === n1) {
      if (mapsAreEqual(m1, m2)) return true

      m2.set(s2[l], m2.get(s2[l]) - 1);
      if (m2.get(s2[l]) === 0) m2.delete(s2[l])
      l++
    }
  }

  return false
};