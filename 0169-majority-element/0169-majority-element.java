class Solution {
    public int majorityElement(int[] nums) {

        int n = nums.length;
        int counter = 1;
        int candidate = nums[0];
        for(int i = 1; i < n; i++) {
            if(counter == 0) {
                candidate = nums[i];
                counter++;
            }
            else {
                if (candidate == nums[i]) {
                    counter++;
                }
                else {
                    counter--;
                }
            }
        }

        return candidate;
        
    }
}