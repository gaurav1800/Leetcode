class Solution {
    public int[] sortedSquares(int[] nums) {
        
        if (nums[0] >= 0) {
            int i=0; 
            while(i < nums.length) {
                nums[i] = square(nums[i]);
                i++;
            }
            return nums;
        }
        
        
        int i=0, j=nums.length-1, idx = nums.length-1;
        
        int[] result = new int[nums.length];
        
        while(idx > -1) {
            
            int isquared = square(nums[i]);
            int jsquared = square(nums[j]);
            
            
            if ( isquared > jsquared) {
                result[idx] = square(nums[i]);
                i++;
            }
            else {
                result[idx] = square(nums[j]);
                j--;
            }
            idx--;
        }
        
        return result;
                
        
        
    }
    
    public int square(int m) {
        return m*m;
    }
}