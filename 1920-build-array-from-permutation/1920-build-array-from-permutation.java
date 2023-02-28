class Solution {
    public int[] buildArray(int[] nums) {
        
        int i = 0;
        int[] result = new int[nums.length];
        while (i != nums.length) {
            result[i] = nums[nums[i]];
            i++;
        }
        
        return result;
        
    }
}