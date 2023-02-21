class Solution {
    public int[] sortedSquares(int[] nums) {
   
        int[] result = new int[nums.length];
        
        int i=0, j=nums.length-1, resultidx = nums.length-1;
        
        while(resultidx > -1) {
            int isquared = nums[i] * nums[i];
            int jsquared = nums[j] * nums[j];
            
            if (isquared > jsquared) {
                result[resultidx--] = isquared;
                i++;
            }
            else {
                result[resultidx--] = jsquared;
                j--;
            }
        }
        
        return result;
        
    }
}