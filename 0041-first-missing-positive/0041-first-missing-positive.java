class Solution {
    public int firstMissingPositive(int[] nums) {
        
        int[] res = new int[nums.length+2];
        
        for(int i=0; i<nums.length; i++) {
            if (nums[i] < 1 || nums[i] > nums.length) {
                
            }
            else {
                res[nums[i]] += 1;
            }
        }
        
        int i=1;
        
        while (res[i] != 0) {
            i++;
        }
        return i;
        
    }
}