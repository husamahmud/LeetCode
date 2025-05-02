function reverse(x: number): number {
  if (x === 0) return 0

  let res = 0
  let absX = Math.abs(x)

  while (absX > 0) {
    if (res > (2 ** 31 - 1) / 10) return 0
    const digit = absX % 10
    res = res * 10 + digit
    absX = Math.floor(absX / 10)
  }

  res = x < 0 ? -res : res
  if (res < -(2 ** 31) || res > 2 ** 31 - 1) return 0
  return res
}
