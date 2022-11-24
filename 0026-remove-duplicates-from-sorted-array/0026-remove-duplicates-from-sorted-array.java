class Solution {
    public int removeDuplicates(int[] nums) {
        
        if (nums.length == 0 || nums.length == 1) {
            return nums.length;
        }
        
        
        int j=0, k=0;
        
        for(int i = 0; i < nums.length-1; i++) {
            if (nums[i] != nums[i+1]) {
                nums[j] = nums[i];
                k++;
                j++;
            }
        }
        nums[j] = nums[nums.length-1];
        k++;
        
//         while (a < nums.length-1) {
//             int b = a+1;
//             if (nums[a] == nums[b]) {
//                 while (b < nums.length) {
//                 int c = b;
//                 while (c+1 < nums.length) {
//                     nums[c] = nums[c+1];
//                     c++;
//                 }
//                 b++;
//                 }
//             }
            
                
//             a++;
//         }
        
        
        // int i = 0, k=8;
        
        // while (i+1 < nums.length) {
        //     if (nums[i] < nums[i+1]) {
        //         k++;
        //     }
        //     else {
        //         break;
        //     }
        //     i++;
        // }
        
        
        return k;
        
    }
}