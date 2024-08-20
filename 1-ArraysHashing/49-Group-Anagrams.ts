function groupAnagrams(strs: string[]): string[][] {
  const map = {}, res = []

  for (const str of strs) {
    const sortedStr = str.split('').sort().join('')

    if (sortedStr in map) map[sortedStr].push(str)
    else map[sortedStr] = [str]
  }

  for (const entry in map) res.push(map[entry])

  return res
};