class Solution {
    public int removeElement(int[] nums, int val) {
        
        
        if (nums.length == 0) {
            return nums.length;
        }
        else if (nums.length == 1 && nums[0] != val) {
            return 1;
        }
        else if (nums.length == 1 && nums[0] == val) {
            return 0;
        }
        
        int j = 0, k = 0;
        
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != val) {
                nums[j] = nums[i];
                j++;
                k++;
            }
        }
        
        
        return k;
        
    }
}