class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int currentSum = 0;
        int result = nums[0];
        
        for(int num : nums) {
            
            if (currentSum < 0) {
                currentSum = 0;
            }
            
            currentSum += num;
            
            result = max(result, currentSum);
        }
        
        return result;
        
    }
};