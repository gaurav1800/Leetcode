class Solution {
    public int search(int[] nums, int target) {
        
        int lo=0, hi=nums.length-1;
        
        while(lo != hi) {
            int mid = (int) Math.floor((lo+hi)/2);
            // if (nums[mid] == target) {
            //     return mid;
            // }
            // else 
            if (nums[mid] < target) {
                lo = mid+1;
            }
            else {
                hi = mid;
            }
        }
        if (nums[lo] == target) {
            return lo;
        }
        else {
            return -1;
        }
        
    }
}