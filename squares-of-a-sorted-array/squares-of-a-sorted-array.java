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
            
            
            if (square(nums[i]) > square(nums[j])) {
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
                
        
//         int[] result = new int[nums.length];
        
//         int i=0, j=nums.length-1, resultidx = nums.length-1;
        
//         while(resultidx > -1) {
//             int isquared = nums[i] * nums[i];
//             int jsquared = nums[j] * nums[j];
            
//             if (isquared > jsquared) {
//                 result[resultidx--] = isquared;
//                 i++;
//             }
//             else {
//                 result[resultidx--] = jsquared;
//                 j--;
//             }
//         }
        
//         return result;
        
    }
    
    public int square(int m) {
        return m*m;
    }
}