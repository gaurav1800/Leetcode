class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        
        
        List<Integer> result = new ArrayList<>();
        
        int j;
        
        for(int i=0; i<nums.length; i++) {
            j = Math.abs(nums[i]) - 1;
            
            if(nums[j] > 0) {
                nums[j] *= -1;
            }
        }
        
        for(int i=0; i<nums.length; i++) {
            if (nums[i] > 0) {
                result.add(i+1);
            }
        }
        
        return result;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
//         List<Integer> result = new ArrayList<>(nums.length);
        
//         int j;
        
//         for(int i=0; i<nums.length; i++) {
            
//             j = Math.abs(nums[i]) - 1;
            
            
//             if(nums[j] > 0) {
//                 nums[j] *= -1;    
//             }
            
//         }
        
//         for(int i=0; i<nums.length; i++) {
//             if(nums[i] > 0) {
//                 result.add(i+1);
//             }
//         }
        
//         return result;
        
        
        
        
    }
}