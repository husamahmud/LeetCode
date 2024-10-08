function removeElement(nums: number[], val: number): number {
  let j = 0;
  for (let n of nums) if (n !== val) nums[j++] = n
  return j
};