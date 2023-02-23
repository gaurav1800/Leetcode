class Solution {
    public int singleNumber(int[] nums) {
   

        if (nums.length == 1) {
            return nums[0];
        }
        
        int result = 0;
        
        for(int i : nums) {
            result ^= i;
        }
        
        return result;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
//         if(nums.length == 1) {
//             return nums[0];
//         }
        
//         int result = 0;
        
//         for(int i = 0; i < nums.length; i++) {
            
//             int counter = 0;
            
//             for(int j = 0; j < nums.length; j++) {
//                 if (nums[i] == nums[j]) {
//                     counter++;
//                 }
//             }
//             if (counter == 1) {
//                 result = nums[i];
//             }
//         }
//         return result;
        
    }
}