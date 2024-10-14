class NumArray {
  private nums: number[]

  constructor(nums: number[]) {
    this.nums = nums
  }

  sumRange(left: number, right: number): number {
    let res: number = 0
    for (let i = left; i <= right; i++) res += this.nums[i]
    return res
  }
}