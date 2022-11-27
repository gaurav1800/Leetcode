class Solution {
    public int searchInsert(int[] nums, int target) {
        
        int i = 0, k = 0;
        
        if (target <= nums[0]) {
            return 0;
        }
        else if (target > nums[nums.length-1]) {
            return nums.length;
        }
        
        
        while(i < nums.length) {
            if (target - nums[i] == 0) {
                k = i;
            }
            else if (target - nums[i] < 0) {
                k = i;
            }
            if (k != 0) {
                break;
            }
            i++;
        }
        return k;
        
        
    }
}