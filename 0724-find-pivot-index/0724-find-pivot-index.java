class Solution {
    public int pivotIndex(int[] nums) {
    
        
        for(int i = 1; i < nums.length; i++) {
            nums[i] += nums[i-1];
        }
    
        int j = nums.length-1;
    
        if (nums[j] == nums[0]) {
            return 0;
        }
        
        
        for(int i=1; i<nums.length; i++) {
            if (nums[j] - nums[i] == nums[i-1]) {
                return i;
            }
        }
        return -1;
        
    }
}