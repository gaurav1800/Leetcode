class Solution {
    public int thirdMax(int[] nums) {
        
        long max1 = Long.MIN_VALUE;
        long max2 = Long.MIN_VALUE;
        long max3 = Long.MIN_VALUE;
        
        for (int num : nums) {

            if (max1 == num || max2 == num || max3 == num) {
                continue;
            }
            

            if (max1 <= num) {
                max3 = max2;
                max2 = max1;
                max1 = num;
            }

            else if (max2 <= num) {
                max3 = max2;
                max2 = num;
            }
            // It is the third greatest number.
            else if (max3 <= num) {
                max3 = num;
            }
        }
        
        if (max3 == Long.MIN_VALUE) {
            int ans = (int) max1;
            return ans;
        }
        
        int ans = (int) max3;
        return ans;
    }
}