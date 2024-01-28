impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        //hash map storing nums as keys and the indices of nums as values
        let mut hm: std::collections::HashMap<i32, i32> = std::collections::HashMap::new();
        
        //for each in input array
        for i in 0..nums.len() {
            //if the hashmap contains the number needed to create target
            if hm.contains_key(&(target - nums[i])) {
                //return the vector with indices need to create target
                return vec![hm[&(target-nums[i])], i as i32];
            }
            //insert the current number and index into hashmap
            hm.insert(nums[i], i as i32);
        }
        return vec![];
    }
}