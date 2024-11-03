function maxArea(height: number[]): number {
  let l: number = 0, r = height.length - 1
  let maxArea: number = 0

  while (l < r) {
    let curArea = Math.min(height[l], height[r]) * (r - l)
    maxArea = Math.max(maxArea, curArea)

    if (height[l] >= height[r]) r--
    else l++
  }

  return maxArea
};