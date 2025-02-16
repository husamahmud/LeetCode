class ArrayWrapper {
  arr: number[]

  constructor(nums: number[]) {
    this.arr = nums
  }

  valueOf(): number {
    return this.arr.reduce((acc, curr) => acc + curr, 0);
  }

  toString(): string {
    return `[${this.arr.toString()}]`
  }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */