class Solution {
    public int[] twoSum(int[] nums, int target) {
                    
        
        int i = 0;
        int result[] = new int[2];
        
        while (i != nums.length-1) {
            int j = i+1;
            while (j != nums.length) {
                if(sum(nums[i], nums[j]) == target) {
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
    
    
    public int sum(int a, int b) {
        return a+b;
    }
}