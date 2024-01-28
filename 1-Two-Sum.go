func twoSum(nums []int, target int) []int {
    m := make(map[int]int)

    for i, num := range nums {
        complement := target - num
        if index, ok := m[complement]; ok {
            return []int{index, i}
        }
        m[num] = i
    }

    return nil
}
