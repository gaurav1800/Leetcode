class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int i=0;
        
        int[] res = new int[2];
        
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