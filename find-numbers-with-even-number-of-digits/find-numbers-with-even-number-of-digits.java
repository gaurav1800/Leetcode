class Solution {
    public int findNumbers(int[] nums) {
        
        int counterEven = 0;
        for(int i=0; i<nums.length; i++) {
            int counter = 0;
            
            while(nums[i] > 0) {
                counter++;
                nums[i] /=10;
            }
            if (counter % 2 == 0) {
                counterEven++;
            }
        }
        
        return counterEven;
        
        
        
    }
}