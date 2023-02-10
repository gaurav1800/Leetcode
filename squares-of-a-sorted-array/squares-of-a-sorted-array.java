class Solution {
    public int[] sortedSquares(int[] nums) {
        
        for(int i=0; i<nums.length; i++) {
            nums[i] = nums[i] * nums[i];
        }
        
        for(int i=1; i<nums.length; i++) {
            
            int j = i;
            int key = nums[i];
            
            while(j>0 && key < nums[j-1]) {
                nums[j] = nums[j-1];
                j--;
            }
            nums[j] = key;
            
        }
        
        return nums;
        
    }
}