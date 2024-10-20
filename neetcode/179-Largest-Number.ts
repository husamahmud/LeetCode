function compare(num1: string, num2: string): number {
  if (num1 + num2 > num2 + num1) return -1;
  if (num1 + num2 < num2 + num1) return 1;
  return 0;
}

function largestNumber(nums: number[]): string {
  let res: string[] = [];

  for (const num of nums) res.push(String(num));

  res.sort((a, b) => compare(a, b));

  if (res[0] === '0') return '0';
  return res.join('');
}
