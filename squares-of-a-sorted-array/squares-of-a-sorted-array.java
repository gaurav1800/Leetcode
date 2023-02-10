class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int[] result = new int[nums.length];
        
        int i=0, j=nums.length-1, iresult=nums.length-1;
        
        
        while(iresult >= 0) {
            int isquared = nums[i] * nums[i];
            int jsquared = nums[j] * nums[j];
            
            if(isquared > jsquared) {
                result[iresult] = isquared; 
                i++;
            }
            else {
                result[iresult] = jsquared;
                j--;
            }
            iresult--;
        }
        
        return result;
    }
}