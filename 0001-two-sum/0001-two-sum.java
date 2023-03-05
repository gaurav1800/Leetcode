class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] res = new int[2];
        
        
//         int lo=0, hi=nums.length-1;
        
//         while(lo<hi) {
//             int mid = (lo+hi) /2;
//             if (nums[lo] + nums[hi] == target) {
//                 res[0] = lo;
//                 res[1] = hi;
//                 return res;
//             }
//             else if (nums[lo] + nums[hi] > target) {
//                 hi = mid;
//             }
//             else {
//                 lo = mid;
//             }
//         }
//         return res;
        
        
        
        
        
        
        
        int i=0;
        while (i < nums.length-1) {
            int j = i+1;
            while (j<nums.length) {
                if (nums[i] + nums[j] == target) {
                    res[0] = i;
                    res[1] = j;
                    return res;
                }
                j++;
            }
            i++;
        }
        return res;
    }
}