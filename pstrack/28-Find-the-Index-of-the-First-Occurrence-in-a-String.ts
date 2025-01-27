function strStr(haystack: string, needle: string): number {
  if (needle.length > haystack.length) return -1

  for (let i = 0; i <= haystack.length - needle.length; i++) {
    if (haystack[i] !== needle[0]) continue

    let count: number = 0
    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] === needle[j]) count++
      else break
    }

    if (count === needle.length) return i
  }
  return -1
};