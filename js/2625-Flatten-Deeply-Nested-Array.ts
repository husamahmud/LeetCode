type MultiDimensionalArray = (number | MultiDimensionalArray)[];

var flat = function (arr: MultiDimensionalArray, n: number): MultiDimensionalArray {
  const res: MultiDimensionalArray = []

  function helper(subArr: MultiDimensionalArray, depth: number) {
    for (const item of subArr) {
      if (Array.isArray(item) && depth > 0) helper(item, depth - 1)
      else res.push(item)
    }
  }

  helper(arr, n)
  return res
};