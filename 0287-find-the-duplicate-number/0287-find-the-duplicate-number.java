class Solution {
    public int findDuplicate(int[] nums) {
        
        int[] res = new int[nums.length];
        
        for(int i=0; i<nums.length; i++) {
            res[nums[i]] += 1;
        }
        
        int i=0;
        while(res[i] < 2) {
            i++;
        }
        return i;
        
    }
}