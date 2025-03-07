function isPrime(num: number): boolean {
  if (num < 2) return false
  if (num === 2 || num === 3) return true
  if (num % 2 === 0 || num % 3 === 0) return false

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }

  return true;
}

function closestPrimes(left: number, right: number): number[] {
  const res: number[] = []

  for (let i = left; i <= right; i++) {
    if (isPrime(i)) {
      const last = res.length ? res[res.length - 1] : -1;
      if (last !== -1 && i - last <= 2) return [last, i];
      res.push(i);
    }
  }

  return res.length === 2 ? res : [-1, -1]
};