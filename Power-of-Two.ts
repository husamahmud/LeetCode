function isPowerOfTwo(n: number): boolean {
  if (n === 1) return true
  if (n < 1) return false
  if (n % 2 === 0) return isPowerOfTwo(n / 2)
  return false
}
