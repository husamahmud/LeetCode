public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        if(nums == null || nums.Length < 2 )
            return new int[2];

        Dictionary<int,int> check = new Dictionary<int,int>() ;

        for(int i = 0; i < nums.Length; i++)
        {
            if(check.ContainsKey(target - nums[i]))
            {
                return new int[]{check[target-nums[i]], i};
            }
            check[nums[i]] = i;
        }
        return new int[]{0,0};
    }
}