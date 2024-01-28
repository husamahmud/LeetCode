
class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var map = [Int: Int]()
        
        for i in 0..<nums.count {
            let complement = target - nums[i]
            if let complementIndex = map[complement] {
                return [complementIndex, i]
            }
            map[nums[i]] = i
        }
        
        return []
    }
}