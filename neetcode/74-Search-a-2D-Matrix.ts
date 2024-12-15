function search(arr: number[], target: number) {
  let l: number = 0, r: number = arr.length - 1

  while (l <= r) {
    const m: number = Math.floor((l + r) / 2)

    if (arr[m] === target) return true
    else if (arr[m] > target) r = m - 1
    else l = m + 1
  }

  return false
}

function searchMatrix(matrix: number[][], target: number): boolean {
  let l = 0, r = matrix.length - 1

  while (l <= r) {
    const m = Math.floor((r - l) / 2) + l

    if (matrix[m][0] <= target && matrix[m][matrix[m].length - 1] >= target) {
      return search(matrix[m], target)
    } else if (matrix[m][0] > target) {
      r = m - 1
    } else {
      l = m + 1
    }
  }

  return false
}
