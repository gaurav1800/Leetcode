class Solution {
    public int findMaxK(int[] nums) {
        
        int i = 0, arrLength = nums.length;
        
        int maxNum = -1;
        
        while (i != arrLength-1) {
            int target = nums[i], j=i+1;
            int negTarget = target*-1;
            
            while ( j != arrLength && negTarget != nums[j]) {
                j++;
            }
            
            if (j != arrLength && negTarget == nums[j]) {
                if (negTarget > target && maxNum < negTarget) {
                    maxNum = negTarget;
                }
                else if (negTarget < target && maxNum < target){
                    maxNum = target;
                }
            }
            i++;
        }
        
        return maxNum;
        
    }
}