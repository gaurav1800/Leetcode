class Solution {
    public int maxSubArray(int[] nums) {
        
        int max = Integer.MIN_VALUE;
        int sum = 0;
        
        for(int num : nums) {
            sum = Math.max(num, num+sum);
            max = Math.max(sum, max);
        }
        return max;
    }
}