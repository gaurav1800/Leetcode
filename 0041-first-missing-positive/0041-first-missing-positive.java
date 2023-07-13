class Solution {
    public int firstMissingPositive(int[] nums) {
        
        int[] result = new int[nums.length+1];
        
        int i = 0;
        while (i < nums.length) {
            if (nums[i] > nums.length || nums[i] < 1) {
                i++;
                continue;
            }
            result[nums[i]] += 1;
            i++;
        }
        
        i = 1;
        while (i < result.length && result[i] != 0) {
            i++;
        }
        return i;
        
    }
}