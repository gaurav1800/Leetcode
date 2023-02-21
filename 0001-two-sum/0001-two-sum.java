class Solution {
    public int[] twoSum(int[] nums, int target) {
                    
        
        int i = 0, len = nums.length;
        int result[] = new int[2];
        
        while (i < len) {
            int j = i+1;
            while (j < len) {
                int sum = nums[i] + nums[j];
                if(sum == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                } 
                j++;                    
            }
            i++;
        }
        return result;
        
    }
}